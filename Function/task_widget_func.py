import sys, json, time, os, platform, threading, logging, coloredlogs
from PySide6.QtWidgets import QApplication, QHeaderView , QDialog, QTextBrowser, QVBoxLayout, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QIcon
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathvalidate import sanitize_filename, sanitize_filepath
from browsermobproxy import Server
from selenium.common.exceptions  import TimeoutException, SessionNotCreatedException, WebDriverException
from UI.task_widget_ui import Ui_Dialog      # 导入对应的UI文件
from Function.static import find_available_port, message_box, mkdir, is_debug

from io import BytesIO
from PIL import Image
# 解决PIL报错的问题
# 除下面的方法，降级 PIL 或修改 ddddocr 的源代码也可以解决该问题
# 确保在调用Image.ANTIALIAS时，Image.ANTIALIAS的默认值是Image.LANCZOS
if not hasattr(Image, 'ANTIALIAS'):
    setattr(Image, 'ANTIALIAS', Image.LANCZOS)
import ddddocr      # 带带弟弟ocr项目

# 创建一个日志记录器
logger = logging.getLogger(__name__)
# 配置coloredlogs，将日志输出到终端
coloredlogs.install(level=is_debug(), fmt='%(asctime)s [%(levelname)s] %(message)s')


class BackgroundTasks(QThread):
    """ 异步加载后台任务 """
    # 结束信号
    finish = Signal()
    result = Signal(dict)

    def __init__(self, option={}):
        super().__init__()
        # 接收参数
        self.url = option.get("current_url")                # 当前url
        self.max_workers = option.get("thread_num", 5)      # 线程数
        self.delay = option.get("delay", 0)                 # 延时
        self.select_mode = option.get("select_mode")        # 选择模式
        self.select_element = option.get("select_element")  # 选择元素
        self.dicts = option.get("dicts")                    # 任务字典
        self.screenshot = option.get("screenshot", False)   # 是否截图
        self.project_dir = option.get("project_dir")        # 项目路径
        self.proxy_mode = option.get("proxy_mode", False)   # 代理模式（True为可以Burp联动的代理服务，False为默认复杂全局流量）
        self.proxy_server = option.get("proxy_url")         # 代理地址
        self.timeout = option.get("timeout", 10)            # 超时时间
        self.retry_num = option.get("retry_num", 1)         # 验证码重试次数
        self.codeInputError = option.get("codeInputError")  # 验证码错误校验内容
        
        # 如果选择而模式不是2，且校验内容为空，则设置重试次数为1次，即只执行一次
        if (self.select_mode != 2) and (not self.codeInputError):
            self.retry_num = 1

        # 如果选择模式为2（即带验证码）则初始化ocr
        if self.select_mode == 2:
            # 初始化ocr对象
            self.ocr = ddddocr.DdddOcr()
        
        # 创建暂停状态
        self.pause_condition = threading.Condition()
        # 是否暂停的标志位
        self.is_paused = False
        # 创建一个线程锁
        self.lock = threading.Lock()

        # 初始化参数
        self.task_num = 0
        # 任务列表
        self.tasks = []
        

    def run(self):
        logger.info(f"{self.url},任务启动")
        # 判断是否使用代理，不使用代理会自动初始化一个代理功能记录全量日志
        if not self.proxy_mode:
            server_port = find_available_port(8080)
            if server_port is None:
                message_box("未找到可用端口", "咋回事铁子，一个能用的端口都找不到呐！")
                logger.warning("开启代理服务：未找到可用端口")
                self.finish.emit()
                return
            else:
                # 初始化代理服务器
                self.server = Server(r".\Server\browsermob-proxy-2.1.4\bin\browsermob-proxy", options={"port":server_port})
                self.server.start()
                proxy = self.server.create_proxy()
                self.proxy_server = proxy.proxy
                proxy.new_har("Complete", options={'captureHeaders':True, 'captureContent':True, 'captureBinaryContent':True})
                logger.info("开启代理服务：端口{}".format(server_port))
        
        # 启动浏览器服务
        self.start_server()     # 提供self.driver_pool

        # 线程池
        self.threads_pool = ThreadPoolExecutor(max_workers=self.max_workers)

        # 提交任务
        for option in self.dicts:
            future = self.threads_pool.submit(self.worker_task, option)
            self.tasks.append(future)
            # print('计划于 {}: {}'.format(option["id"], future))
        
        # 等待任务结束
        for future in as_completed(self.tasks):
            result = future.result()
            # 发出单个结果信号
            self.result.emit(result)

        logger.info(f"{self.url}任务结束")

        if not self.proxy_mode:
        # 获取新网页记录的HAR数据
            # 以创建新页面记录的时间戳为文件名
            har_path = sanitize_filepath(self.project_dir + "/Har/" + "Complete.har")
            logger.info("保存HAR数据：{}".format(har_path))
            # 将数据保存到文件或进行其他处理
            with open(har_path, 'w', encoding='utf-8') as f:
                f.write(json.dumps(proxy.har, indent=2))
            # 关闭代理端口
            proxy.close()
            # 停止代理服务
            self.server.stop()

        # 发送任务结束信号
        self.finish.emit()
        # 结束服务
        self.stop_server()

    def stop_server(self):
        """ 结束所有服务 """
        # 结束所有web服务
        for i in self.driver_pool:
            self.driver_pool[i][1].close()
            # self.driver_pool[i][1].service.stop()
            self.driver_pool[i][1].quit()
        """ browsermobproxy库关闭关不干净，所以下面再主动关闭开启的端口 """
        # 获取当前操作系统
        current_os = platform.system()
        # 根据不同的操作系统执行不同的命令
        try:
            if current_os == "Windows":
                # 在Windows上执行相关操作
                find_port = 'netstat -aon | findstr %s' % self.server.port
                result = os.popen(find_port)
                text = result.read()
                result.close()
                pid_line = text.split('\n', 1)[0]
                pid = pid_line.replace(" ", "").split("LISTENING")[1]
                
                find_kill = 'taskkill /F /PID %s' % pid
                result = os.popen(find_kill)
                result.close()
                
            elif current_os == "Linux":
                # 在Linux上执行相关操作
                command = f'lsof -t -i :%s' % self.server.port
                pid = os.popen(command).read().strip()
                # 使用 kill 命令终止指定 PID 的进程
                os.system(f'kill -9 {pid}')
        except Exception as e:
            print(f"Error: {e}")
        logger.info("代理服务和浏览器服务关闭")
            
    def start_server(self):
        # print(self.proxy_server)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server={self.proxy_server}')
        chrome_options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
        chrome_options.add_argument("--incognito")  # 无痕模式
        chrome_options.add_argument('--no-sandbox') # 关闭沙盒启动
        chrome_options.add_argument("--disable-blink-features=AutomationControlled") # 禁用 blink 特征
        chrome_options.add_argument('--headless')    # 隐藏浏览器,不提供可视化页面
        chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        chrome_options.add_experimental_option('useAutomationExtension', False) # # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 正常浏览器window.navigator.webdriver的值为undefined,而使用selenium访问则该值为true,该方法规避这种风险。
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])    # 禁止 chromedriver 日志写屏
        chrome_options.add_argument('--disable-usb-devices')    # 禁用 USB 设备
        chrome_options.add_argument('--disable-plugins')
        chrome_options.add_argument('--disable-extensions')
        # 需要识别验证码的时候加载图片，其他模式不加载图片, 提升速度
        if self.select_mode != 2:
            chrome_options.add_argument('--blink-settings=imagesEnabled=false')  

        logger.info("浏览器驱动加载中，请稍后...")
        # 浏览器驱动池，根据最大线程数创建
        self.driver_pool = {}
        for num in range(self.max_workers):
            try:
                self.driver_pool[f"driver-{num}"] = [False, webdriver.Chrome(options=chrome_options)]
            except SessionNotCreatedException:
                self.driver_pool[f"driver-{num}"] = [False, webdriver.Chrome(options=chrome_options)]
        logger.info("浏览器驱动加载完毕")

    def worker_task(self, option):
        """ 任务处理 """
        id = option.get("id")
        username = option.get("username")
        password = option.get("password")

        retry_num = self.retry_num
        # 选中的浏览器服务
        webdriver = None

        # 运行任务
        result = option
        result["url"] = self.url
        result["timeout"] = False
        result["screenshot"] = self.screenshot
        # 设置线程锁防止冲突
        with self.lock:
            # 选择浏览器驱动
            while webdriver is None:
                for i in self.driver_pool:
                    if not self.driver_pool[i][0]:
                        # 选中的web浏览器服务
                        webdriver = i
                        # 设置浏览器驱动被使用
                        self.driver_pool[i][0] = True
                        break
                driver = self.driver_pool[webdriver][1]
        # print(f"这是{id}的web服务：",webdriver, driver)
        # 设置隐式超时时间，等待元素加载
        driver.set_page_load_timeout(self.timeout)
        driver.implicitly_wait(self.timeout)

        try:
            while retry_num > 0:
                retry_num -= 1
                # 清除缓存和Cookie
                driver.delete_all_cookies()
                
                # 打开网站
                driver.get(self.url)
                # 选择模式为0或2的都带username元素
                if self.select_mode in [0, 2]:
                    username_input = driver.find_element(By.XPATH, self.select_element["userElement"][2])
                    username_input.send_keys(username)
                
                # 如果是2号模式，则加上验证码模块
                if self.select_mode == 2:
                    code = driver.find_element(By.XPATH, self.select_element["codeElement"][2])
                    # 坐标
                    x, y = code.location.values()
                    # 宽高
                    h, w = code.size.values()
                    # 把截图以二进制形式的数据返回
                    image_data = driver.get_screenshot_as_png()
                    # 以新图片打开返回的数据
                    screenshot = Image.open(BytesIO(image_data))
                    # 对截图进行裁剪
                    img = screenshot.crop((x, y, x + w, y + h))
                    # 识别验证码
                    res = self.ocr.classification(img)
                    # 保存验证码图片
                    img_name = sanitize_filename(f'{id}_{res}.png', "_")
                    img_path =  sanitize_filepath(self.project_dir + "/Captcha/" + img_name, "_")
                    img.save(img_path)
                    # 输入验证码
                    code_input = driver.find_element(By.XPATH, self.select_element["codeInputElement"][2])
                    code_input.send_keys(res)
                
                # 所有模式都带password元素和登录按钮
                password_input = driver.find_element(By.XPATH, self.select_element["passElement"][2])
                password_input.send_keys(password)

                # 找到登录按钮并单击
                login_button = driver.find_element(By.XPATH, self.select_element["loginElement"][2])
                login_button.click()

                # 延迟，等待加载（也可作为访问间隔）
                time.sleep(self.delay)

                # 选择模式为2,且校验内容不为空，判断获取的页面内容是否存在验证码输入错误提示
                if (self.select_mode == 2) and self.codeInputError:
                    if self.codeInputError not in driver.page_source:
                        break

            # 截图
            if self.screenshot:
                file_name = sanitize_filename(f"{id}-{username}-{password}.png", "_")
                file_path = sanitize_filepath(self.project_dir + "/ScreenShot/" + file_name)
                driver.get_screenshot_as_file(file_path)
            else:
                file_path = None

            result["screenshot_path"] = file_path
            result["url"] = driver.current_url
            result['page_source'] = driver.page_source
        except (TimeoutException, WebDriverException):
            result["timeout"] = True
            result["screenshot"] = False    # 超时无截图
        except Exception as e:
            print("任务运行错误：", e)
            logger.error(f"任务运行错误：{e}")

        result["length"] = len(driver.page_source)
        # 恢复webdriver为不使用状态
        self.driver_pool[webdriver][0] = False

        # 判断暂停标志状态
        with self.pause_condition:
                while self.is_paused:
                    # 等待继续信号
                    self.pause_condition.wait()
        
        return result


class Main(QDialog, Ui_Dialog):
    def __init__(self, option, config_str):
        super().__init__()
        self.setupUi(self)
        self.icon_bamboo = QIcon("icon/bamboo.png")
        self.setWindowIcon(self.icon_bamboo)
        
        self.option = option
        self.config_str = config_str
        self.dicts = []     # 任务列表
        self.results = {}
        self.data = []

        # 项目路径
        self.project_dir = sanitize_filepath("Output/"+sanitize_filename(str(int(time.time())) + "_" +self.option['current_url'], "_"))
        # 需要创建的目录列表
        self.dirs = [self.project_dir]
        # 根据模式选择创建目录
        if not self.option["proxy_mode"]:
            self.dirs.append(self.project_dir + "/Har")
        if self.option["screenshot"]:
            self.dirs.append(self.project_dir + "/Screenshot")
        if self.option["select_mode"] == 2:
            self.dirs.append(self.project_dir + "/Captcha")

        # 初始化UI的逻辑函数
        self._logic_func()
        # 初始化字典，如果字典为空则结束任务，否则开启任务
        self.initDict()
            

    def _logic_func(self):
        # 初始化任务窗口标题
        self.setWindowTitle(f"任务：{self.option['current_url']}")

        # 设置表格列自动补齐
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 查看参数配置
        self.pushButton_config.clicked.connect(self.__config_func)
        # 连接列表头点击事件
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortTable)
        # 表格项选中更新tabWidget
        self.tableWidget.cellClicked.connect(self.update_tabWidget)
        # 暂停爆破
        self.pushButton_pause.clicked.connect(self.__pause_func)
        # 终止爆破
        self.pushButton_stop.clicked.connect(self.__stop_func)

    def initDict(self):
        """初始化任务表"""
        # 获取字典表
        dict_table = self.option['code_book']
        if 'userElement' in dict_table.keys():
            user_code_book = dict_table['userElement'].get_all_items()
            # user_code_book = dict_table['userElement'] # 测试使用
            # print(self.user_code_book)
        else:
            user_code_book = None

        if 'passElement' in dict_table.keys():
            pass_code_book = dict_table['passElement'].get_all_items()
            # pass_code_book = dict_table['passElement'] # 测试使用
            # print(self.pass_code_book)
        else:
            pass_code_book = None

        # 生成任务字典
        blast_mode = self.option["blast_mode"]
        # 设置参数
        option = {}
        task_id = 0
        # Cluster bomb:集束炸弹，使用穷举法，对每个目标都遍历字典
        if blast_mode == 0:
            for user in user_code_book:
                for password in pass_code_book:
                    task_id += 1
                    option = {'id':task_id, 'username':user, 'password':password}
                    self.dicts.append(option)
        # Sniper:阻击手，使用一个字典，将目标逐个进行遍历替换
        elif blast_mode == 1:
            for password in self.pass_code_book:
                task_id += 1
                option = {'id':task_id, 'username':None, 'password':password}
                self.dicts.append(option)
        # Battering ram:攻城锤，使用一个字典，将所有目标进行同时替换再发出
        elif blast_mode == 2:
            for item in self.pass_code_book:
                task_id += 1
                option = {'id':task_id, 'username':item, 'password':item}
                self.dicts.append(option)
        # Pitchfork:草叉模式，对每个目标单独设置字典，按照一一对应的关系取最少的组合
        elif blast_mode == 3:
            min_list_num = len(self.user_code_book) if len(self.user_code_book) < len(self.pass_code_book) else len(self.pass_code_book)
            for i in range(min_list_num):
                task_id += 1
                option = {'id':task_id, 'username':self.user_code_book[i], 'password':self.pass_code_book[i]}
                self.dicts.append(option)

        self.task_num = len(self.dicts)
        # 进度条任务数计算，如果任务数为0，则直接完成任务，下面的不再运行
        if self.task_num:
            # 进度条步长计算
            self.progress_step = 100 / self.task_num
            # 开启任务
            self.startTask()
        else:
            message_box("字典错误", "账号密码没有设置啊喂！！！")
            logger.warning("字典为空")
            self.__stop_func()

    def closeEvent(self, event):
        """ 重写关闭窗口事件 """
        logging.shutdown()
        return super().closeEvent(event)

    def startTask(self):
        # 批量创建文件夹
        for i in self.dirs:
            mkdir(i)
        # 启动任务并更新进度
        self.progressBar.setValue(0)
        option = {
            "current_url": self.option['current_url'],
            'thread_num': self.option['thread_num'], 
            "delay": self.option['delay'],
            "select_mode": self.option['select_mode'],
            "select_element": self.option['select_element'],
            "project_dir": self.project_dir,
            "dicts": self.dicts, 
            "screenshot": self.option["screenshot"],
            "proxy_mode": self.option["proxy_mode"],
            "proxy_url": self.option["proxy_url"],
            "timeout": self.option["timeout"],
            "codeInputError":self.option["codeInputError"],
            "retry_num":self.option["retry_num"],
            }
        # 初始化后台任务
        self.background_task_thread = BackgroundTasks(option)
        self.background_task_thread.result.connect(self.update_tableWidget)
        self.background_task_thread.result.connect(self.update_progressBar)
        self.background_task_thread.finish.connect(self.finish_task)
        # 后台任务启动
        self.background_task_thread.start()

        
    def __config_func(self):
        """ 查看配置参数 """
        dialog = QDialog(self)
        layout = QVBoxLayout()
        dialog.setWindowTitle("任务参数配置信息")
        text_browser = QTextBrowser()
        text_browser.setPlainText(self.config_str)
        layout.addWidget(text_browser)

        dialog.setLayout(layout)
        dialog.show()

    def __pause_func(self):
        """ 暂停爆破 """
        with self.background_task_thread.pause_condition:
            # 继续执行
            if self.background_task_thread.is_paused:
                self.background_task_thread.is_paused = False
                # 通知等待的任务继续执行
                self.background_task_thread.pause_condition.notify_all()  
                self.pushButton_pause.setText("暂停任务")
                logger.info(f"{self.option['current_url']}任务已暂停")
                self.label.setText("运行中")
            # 暂停任务
            else:
                self.background_task_thread.is_paused = True
                self.pushButton_pause.setText("继续任务")
                logger.info(f"{self.option['current_url']}任务继续")
                self.label.setText("已暂停")
             
    def __stop_func(self):
        """ 停止爆破 """
        try:
            # 关闭线程池
            self.background_task_thread.threads_pool.shutdown()
            self.progressBar.value(100)
        except:
            pass
        logger.info(f"{self.option['current_url']}任务已停止")
        self.label.setText("已停止")
        self.pushButton_pause.setEnabled(False)
        self.pushButton_stop.setEnabled(False)
        

    def finish_task(self):
        """ 任务结束 """
        try:
            logger.info(f"{self.option['current_url']}任务已完成")
            self.label.setText("任务完成")
            self.progressBar.setValue(100)
            self.pushButton_pause.setEnabled(False)
            self.pushButton_stop.setEnabled(False)
            with open(self.project_dir + "/result.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(self.results, indent=2))
        except AttributeError:
            pass

    def populateTable(self):
        """ 填充表格 """
        self.tableWidget.setRowCount(len(self.data))
        for row, rowData in enumerate(self.data):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)

    def sortTable(self, column):
        """ 排序表格 """
        current_order = self.tableWidget.horizontalHeader().sortIndicatorOrder()
        self.data.sort(key=lambda x: x[column], reverse=current_order == Qt.DescendingOrder)
        self.populateTable()

    def update_tableWidget(self, result):
        """ 更新表格 """
        self.results[result['id']] = result
        # 当前行数
        row = self.tableWidget.rowCount()
        # 从当前位置插入一行
        self.tableWidget.insertRow(row)

        data = [
            result['id'],
            result['url'], 
            result['username'],
            result['password'],
            result["timeout"],
            result["length"]
        ]
        self.data.append(data)
        self.populateTable()

    def update_progressBar(self, result):
        """ 更新进度条 """
        current_progress = result["id"] * self.progress_step
        self.progressBar.setValue(current_progress)

    def update_tabWidget(self, row, col):
        """ 更新选项卡组件 """
        if row >= 0:
            row_data = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    value = item.text()
                    row_data.append(value)
            id = int(row_data[0])
            data = self.results[id]
            try:
                self.plainTextEdit_html.setPlainText(data['page_source'])
            except:
                self.plainTextEdit_html.setPlainText("未获取到页面html")
            if data['screenshot']:
                self.scrollArea.setImage(data['screenshot_path'])
                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    option = {
        'current_url': 'http://192.168.99.114:5000',
        'blast_mode': 0,
        'thread_num': 2,
        'delay': 0.0,
        'timeout': 10.0,
        'select_mode': 0,
        'select_element': {
                'userElement': ['<input type="text" id="username" name="username" required="" style="">', '用户名元素', '//*[@id="username"]'], 
                'passElement': ['<input type="password" id="password" name="password" required="" style="">', '密码元素', '//*[@id="password"]'], 
                'loginElement': ['<input type="submit" value="Login" style="">', '登录元素', '/html/body/form[1]/input[3]']
            }, 
        'code_book': {'userElement': ['a','admin'], 'passElement': ['password','a']}, 
        'screenshot': True, 
        'proxy_mode': False, 
        'proxy_url': ''}
    window = Main(option=option, config_str="123")
    window.show()

    sys.exit(app.exec())