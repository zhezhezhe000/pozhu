import sys, logging, coloredlogs
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QInputDialog
from PySide6.QtCore import QUrl, Slot, QObject, Signal
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtGui import QIcon
from UI.main_ui_ui import Ui_MainWindow  # 导入相关UI文件
from Function import code_book_func, task_widget_func
from Function.static import message_box, is_debug, load_config     # 公用函数
from UI.about_ui import Ui_Dialog
"""### 这个版本的js获取元素方式是创建web通道，本地加载html获取xpath ###"""
# 加载json文件
config = load_config()

class ElementClickHandler(QObject):
    """
    自定义插槽：元素点击处理
    """
    clicked = Signal(str, str)
    @Slot(str, str)
    def handleElementClick(self, html, xpath):
        self.clicked.emit(html, xpath)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化ui函数
        self.initUI()

        # 初始化选项参数
        self.initOption()

    def initOption(self):
        self.setWindowTitle(f"破竹v{config['version']}      by：迷迷惘惘（严禁用于非授权使用及非法测试用途！）【内部使用，切勿外传】")
        # 加载icon
        self.icon_selected = QIcon("icon/Selected.svg")
        self.icon_notSelected = QIcon("icon/notSelected.svg")
        self.icon_bamboo = QIcon("icon/bamboo.png")
        self.setWindowIcon(self.icon_bamboo)

        # 创建一个日志记录器
        self.logger = logging.getLogger(__name__)
        # 配置coloredlogs，将日志输出到终端
        coloredlogs.install(level=is_debug(), fmt='%(asctime)s [%(levelname)s] %(message)s')

        # 一些信号/状态/参数
        self.current_url = None         # 当前打开的url
        self.link_open_status = False   # 链接打开状态（是否打开网站）
        self.selectElement = None       # 元素选择判断
        
        self.userElement = None         # 用户名元素内容
        self.passElement = None         # 密码元素内容
        self.codeElement = None         # 验证码元素内容
        self.codeInputElement = None    # 验证码输入框元素内容
        self.loginElement = None        # 登录元素选择
        
        self.userElementXpath = None         # 用户名元素xpath
        self.passElementXpath = None         # 密码元素xpath
        self.codeElementXpath = None         # 验证码元素xpath
        self.codeInputElementXpath = None    # 验证码输入框元素xpath
        self.loginElementXpath = None        # 登录元素xpath

        self.element_mode = [[0, 1, 4], [1, 4], [0, 1, 2, 3, 4]]    # 选择模式：账号、密码 | 单密码 | 账号、密码、验证码 （默认都加入登录元素）
        self.element = {
            "userElement":[self.ui.pushButton_selectUser, self.userElement, "用户名元素", self.userElementXpath, self.userCodeBook],
            "passElement":[self.ui.pushButton_selectPass, self.passElement, "密码元素", self.passElementXpath, self.passCodeBook],
            "codeElement":[self.ui.pushButton_selectCode, self.codeElement, "验证码元素", self.codeElementXpath],
            "codeInputElement":[self.ui.pushButton_selectCodeInput, self.codeInputElement, "验证码输入元素", self.codeInputElementXpath],
            "loginElement":[self.ui.pushButton_selectLogin, self.loginElement, "登录元素", self.loginElementXpath],
        }   # 元素值
        self.task_dialogs = []  # 存储打开的任务子窗口的列表

        # 更新配置信息
        self.__update_config_label()

    def initUI(self):
        """ 初始化UI """
        # 初始化密码本
        self._code_book_widget()
        # 调用逻辑函数(绑定槽函数)
        self._logic_func()
        # 初始化爆破模式标签描述
        self.__blast_mode_func()
        
    def closeEvent(self, event):
        """ 重写关闭窗口事件 """
        # 关闭主窗口时关闭所有子窗口
        for dialog in self.task_dialogs:
            dialog.close()
        event.accept()
        # 退出驱动
        try:
            logging.shutdown()
        except:
            pass

    """
    内部函数：初始化操作
    """
    def _code_book_widget(self):
        # 初始化密码本组件
        self.userCodeBook = code_book_func.Main()
        self.passCodeBook = code_book_func.Main()
        # 将这两个组件加入到tabWidget
        self.ui.tabWidget.addTab(self.userCodeBook, "用户名")
        self.ui.tabWidget.addTab(self.passCodeBook, "密码")

    def _logic_func(self):
        """ 绑定信号方法 """
        # menu菜单
        self.ui.actionabout.triggered.connect(self.__about)
        # 打开网站
        self.ui.pushButton_open.clicked.connect(self.__open_link_func)
        self.ui.pushButton_open.clicked.connect(self.__update_config_label)
        # 开始爆破
        self.ui.pushButton_start.clicked.connect(self.__start_func)

        # 下拉框选中操作
        self.ui.comboBox_blast.currentIndexChanged.connect(self.__blast_mode_func)
        self.ui.comboBox_blast.currentIndexChanged.connect(self.__update_config_label)
        self.ui.comboBox_select.currentIndexChanged.connect(self.__select_mode_func)
        self.ui.comboBox_select.currentIndexChanged.connect(self.__update_config_label)

        # 数字框变化设置
        self.ui.spinBox_thread.valueChanged.connect(self.__update_config_label)
        self.ui.doubleSpinBox_delay.valueChanged.connect(self.__update_config_label)
        self.ui.doubleSpinBox_timeout.valueChanged.connect(self.__update_config_label)
        self.ui.spinBox_retryNum.valueChanged.connect(self.__update_config_label)

        # 复选框状态
        self.ui.checkBox_screenshot.stateChanged.connect(self.__update_config_label)
        self.ui.checkBox_proxy.stateChanged.connect(self.__proxy_func)
        self.ui.checkBox_proxy.stateChanged.connect(self.__update_config_label)
        self.ui.checkBox_standby.stateChanged.connect(self.__standby_func)

        # 元素选择
        self.ui.pushButton_selectLogin.clicked.connect(self.__select_login)
        self.ui.pushButton_selectUser.clicked.connect(self.__select_user)
        self.ui.pushButton_selectPass.clicked.connect(self.__select_pass)
        self.ui.pushButton_selectCode.clicked.connect(self.__select_code)
        self.ui.pushButton_selectCodeInput.clicked.connect(self.__select_codeInput)

        # 创建 Web 通道 -> python 和 html 通信使用
        self.channel = QWebChannel()
        self.handler = ElementClickHandler()    # 初始化自定义插槽，在 JavaScript 中被调用，以便在点击元素时执行相应的操作。
        self.channel.registerObject("handler", self.handler)    # 将对象self.handler注册到 Web 通道中,并将其命名为 "handler",这样，JavaScript 代码可以通过 qt.webChannelTransport.handler 访问该对象。
        self.ui.webEngineView.page().setWebChannel(self.channel) # 设置web通道对象，以便 JavaScript 代码可以通过 qt.webChannelTransport 访问 Python 代码。
        # 自定义信号点击操作
        self.handler.clicked.connect(self.__handle_element_click)


    """
    内部函数：槽函数
    """
    def __about(self):
        """菜单-关于"""
        info_dialog = QDialog(self)
        about = Ui_Dialog()
        about.setupUi(info_dialog)
        about.version.setText(f"版本：v{config['version']}")
        info_dialog.show()

    def __blast_mode_func(self):
        """ 选择爆破模式 """
        blast_index = self.ui.comboBox_blast.currentIndex()
        if blast_index in [0, 1]:
            self.ui.comboBox_select.setCurrentIndex(blast_index)

        label_text = [
                    "Cluster bomb:集束炸弹，使用穷举法，对每个目标都遍历字典\t",
                    "Sniper:阻击手，使用一个字典，将目标逐个进行遍历替换\t",
                    "Battering ram:攻城锤，使用一个字典，将所有目标进行同时替换再发出\t",
                    "Pitchfork:草叉模式，对每个目标单独设置字典，按照对应的关系取最少的组合"]

        self.ui.label_des.setText(label_text[blast_index])
        self.ui.tabWidget.setCurrentIndex(1 if blast_index in [1,2] else 0)
        self.ui.tabWidget.setTabEnabled(0, False if blast_index in [1,2] else True)


    def __open_link_func(self):
        """ 打开网站 """
        # 每次打开网站运行一次选择元素，恢复元素默认值
        self.__select_mode_func()
        # 绑定信号连接，当网页加载完成后获取HTML内容
        self.ui.webEngineView.loadFinished.connect(self.__get_html_content)
        # 加载网页
        q = QUrl(self.ui.lineEdit_target.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.ui.webEngineView.setUrl(q)
        self.current_url = self.ui.webEngineView.url().toString()
        
    def __start_func(self):
        """ 开始爆破 """
        option = self.get_option()
        # 如果使用代理则代理地址不能为空
        if option["proxy_mode"] and option["proxy_url"] == "":
            message_box("proxy", "启用了代理，那你设置地址啊\n一用一个不吱声…")
            self.logger.warning("未设置代理地址")
        # 当前url和元素选择不能为空
        elif (option["current_url"] == None) or (None in option["select_element"]):
            message_box("element", "打开网站，选择元素啊，大兄弟~")
            self.logger.warning("未选择元素")
        else:
            self.logger.info(f"开始任务{option['proxy_url']}")
            dialog = task_widget_func.Main(option, self.ui.textBrowser_config.toPlainText())
            self.task_dialogs.append(dialog)
            dialog.show()

    def __select_mode_func(self):
        """ 选择元素选项模式 """
        status_num = self.ui.comboBox_select.currentIndex()
        # 如果选择模式1则设置密码本只开启密码项
        self.userCodeBook.setEnabled(False if status_num == 1 else True)
        self.ui.tabWidget.setCurrentIndex(1 if status_num == 1 else 0)

        # 如果选择模式2则设置验证码错误提示输入框启用
        self.ui.lineEdit_codeInputError.setEnabled(True if status_num == 2 else False)

        # 还原按钮变量
        for i in self.element:
            self.element[i][0].setEnabled(False)    # 禁用所有按钮
            self.element[i][1] = None   # 设置所有元素的html为none
            self.element[i][3] = None   # 设置所有元素的xpath为none
        # 启用指定按钮
        for i in self.element_mode[status_num]:
            list(self.element.values())[i][0].setEnabled(True)

    def __standby_func(self):
        """ 备用模式--获取手动输入的xpath """
        # 恢复xpath元素为none
        self.__select_mode_func()
        self.__update_config_label()
        if self.ui.checkBox_standby.isChecked():
            self.logger.info("备用模式启动")
            self.ui.webEngineView.setEnabled(False)
            self.ui.pushButton_selectLogin.clicked.disconnect(self.__select_login)
            self.ui.pushButton_selectUser.clicked.disconnect(self.__select_user)
            self.ui.pushButton_selectPass.clicked.disconnect(self.__select_pass)
            self.ui.pushButton_selectCode.clicked.disconnect(self.__select_code)
            self.ui.pushButton_selectCodeInput.clicked.disconnect(self.__select_codeInput)

            self.ui.pushButton_selectLogin.clicked.connect(lambda: self.get_xpath("loginElement"))
            self.ui.pushButton_selectUser.clicked.connect(lambda: self.get_xpath("userElement"))
            self.ui.pushButton_selectPass.clicked.connect(lambda: self.get_xpath("passElement"))
            self.ui.pushButton_selectCode.clicked.connect(lambda: self.get_xpath("codeElement"))
            self.ui.pushButton_selectCodeInput.clicked.connect(lambda: self.get_xpath("codeInputElement"))
        else:
            self.logger.info("备用模式关闭")
            self.ui.webEngineView.setEnabled(True)
            self.ui.pushButton_selectLogin.clicked.connect(self.__select_login)
            self.ui.pushButton_selectUser.clicked.connect(self.__select_user)
            self.ui.pushButton_selectPass.clicked.connect(self.__select_pass)
            self.ui.pushButton_selectCode.clicked.connect(self.__select_code)
            self.ui.pushButton_selectCodeInput.clicked.connect(self.__select_codeInput)

    def __proxy_func(self):
        """ 是否开启代理功能 """
        self.ui.lineEdit_proxy.setEnabled(self.ui.checkBox_proxy.isChecked())

    def __select_login(self):
        """ 选择登录元素 """
        self.selectElement = "loginElement"
        self.__check_link_open_status()
    
    def __select_user(self):
        """ 选择用户名元素 """
        # 绑定自定义槽函数到信号
        self.selectElement = "userElement"
        self.__check_link_open_status()

    def __select_pass(self):
        """ 选择密码元素 """
        self.selectElement = "passElement"
        self.__check_link_open_status()
    
    def __select_code(self):
        """ 选择验证码元素 """
        self.selectElement = "codeElement"
        self.__check_link_open_status()

    def __select_codeInput(self):
        """ 选择验证码输入框元素 """
        self.selectElement = "codeInputElement"
        self.__check_link_open_status()

    def __handle_element_click(self, html, xpath):
        """ 处理html点击事件的槽函数 """
        # print(html, xpath)
        # 根据选择的元素设置html
        self.element[self.selectElement][1] = html
        self.element[self.selectElement][3] = xpath
        self.__update_config_label()
        
    
    """
    内部函数：方法调用
    """
    def get_option(self):
        """ 获取配置信息 """
        select_element = {} # 元素选择，返回元素名和元素值
        code_book = {}  # 密码本
        element_mode = self.element_mode[self.ui.comboBox_select.currentIndex()]
        
        for i in element_mode:    
            # 重组元素，只获取想要的元素，格式为 {元素名:[元素html对象, 描述, 元素xpath对象]}
            select_element[list(self.element.keys())[i]] = list(self.element.values())[i][1:4]
            # 获取密码本，用户或密码列表，格式为{元素名:密码本对象}
            if i in [0, 1]:
                code_book[list(self.element.keys())[i]] = list(self.element.values())[i][4]

        option = {
            "current_url": self.current_url,                                    # 当前url
            "blast_mode": self.ui.comboBox_blast.currentIndex(),                # 爆破模式
            "thread_num": self.ui.spinBox_thread.value(),                       # 线程
            "delay": self.ui.doubleSpinBox_delay.value(),                       # 延时
            "timeout":self.ui.doubleSpinBox_timeout.value(),                    # 超时
            "select_mode": self.ui.comboBox_select.currentIndex(),              # 选择模式
            "select_element": select_element,                                   # 元素内容
            "code_book": code_book,                                             # 密码本对象
            "screenshot": self.ui.checkBox_screenshot.isChecked(),              # 是否截图
            "proxy_mode": self.ui.checkBox_proxy.isChecked(),                   # 是否开启代理
            "proxy_url": self.ui.lineEdit_proxy.text(),                         # 代理地址
            "codeInputError":self.ui.lineEdit_codeInputError.text().strip(),    # 验证码错误提示
            "retry_num":self.ui.spinBox_retryNum.value()                        # 验证码错误重试数
        }
        return option
    
    def __update_config_label(self):
        """ 更新配置显示标签 """
        blast_mode = ["Cluster bomb:集束炸弹", "Sniper:阻击手", "Battering ram:攻城锤", "Pitchfork:草叉模式"]
        select_mode = ["账号、密码", "单密码", "账号、密码、验证码"]
        option = self.get_option()
        select_element_text = ""
        for i in option["select_element"].values():
            html, des, xpath = i
            select_element_text += f"{'---'*5}\n" 
            select_element_text += f"{des}：{html}\nXPath：{xpath}\n"
        
        # 设置不同状态的icon
        for i in self.element.values():
            i[0].setIcon(self.icon_notSelected if i[3] is None else self.icon_selected)

        retry_num_text = f"验证码错误重试数：{option['retry_num']}\n" if option["select_mode"] == 2 else ""
        code_error_text = f"验证码错误提示：{option['codeInputError']}\n" if option["select_mode"] == 2 else ""

        text =  f'{"#"*20}\n'\
                f'爆破模式：{blast_mode[option["blast_mode"]]}\n线程数：{option["thread_num"]}\n延时：{option["delay"]}s\n超时：{option["timeout"]}\n{retry_num_text}{code_error_text}'\
                f'截图功能：{"已开启" if option["screenshot"] else "未开启"}\n代理功能：{"已开启" if option["proxy_mode"] else "未开启"}\n备用模式：{"已启用" if self.ui.checkBox_standby.isChecked() else "未启用"}\n'\
                f'选择模式：{select_mode[option["select_mode"]]}\n元素选择：\n{select_element_text}'\
                f'{"#"*20}'
        self.ui.textBrowser_config.setText(text)

    
    def __get_html_content(self):
        """ 获取html内容 """
        self.link_open_status = True
        # 网站加载完成后断开加载结束的连接信号，防止后面setHtml的时候造成死循环
        self.ui.webEngineView.loadFinished.disconnect(self.__get_html_content)

        # 由于无法直接同网络上的页面进行通信，所以采用获取html代码二次处理后在本地获取指定的参数后再进行操作的方式获取数据
        # 获取网页的HTML内容，并将返回值传回回调函数，进行二次处理html内容
        self.ui.webEngineView.page().toHtml(self.__process_html_content)

    def __process_html_content(self, html_content):
        """ 处理HTML内容 """
        self.current_html_content = html_content
        # 在此处处理HTML内容，插入js代码，以便js和python进行通信
        js_code = """<script src="qrc:///qtwebchannel/qwebchannel.js"></script>"""
        html = self.__insert_string_before_head(html_content, js_code)
        # print(html)
        with open("test.html",'w', encoding="utf-8")as f:
            f.write(html)
        self.ui.webEngineView.setHtml(html)

    def __insert_string_before_head(self, html, string_to_insert):
        """ 查找</head>位置，并插入指定代码 """
        # 查找 `</head>` 标签的位置
        head_end = html.find('</head>')

        if head_end != -1:
            # 如果找到 `</head>`，则插入指定字符串
            updated_html = html[:head_end] + string_to_insert + html[head_end:]
            return updated_html
        else:
            # 如果没有找到 `</head>`，则直接返回指定代码+原始字符串
            return string_to_insert + html

    def __select_element(self):
        """ 选择html元素"""
        js_script = '''
            document.body.style.cursor = 'crosshair';   // 修改光标样式为十字

            var element;
            disableLinksAndButtons(); // 禁用链接和按钮的默认行为

            // 绑定事件
            document.addEventListener('mouseover', mouseoverEvent); // 鼠标悬停
            document.addEventListener('mouseout', mouseoutEvent);   // 鼠标移出
            document.addEventListener('click', clickEvent);         // 鼠标点击

            // 鼠标悬停事件
            function mouseoverEvent(event) {
                element = event.target;
                element.style.outline = '2px solid red';    // 设置边框样式
            }
            // 鼠标移出事件
            function mouseoutEvent(event){
                element.style.outline = '';     // 清空边框样式
            }
            // 鼠标点击事件
            function clickEvent(event){
                element.style.outline = '';
                var html = element.outerHTML;   // 获取元素html代码
                var xpath = getXPath(element);  // 获取元素xpath
                // 创建和python的通信对象, 传递参数到slot
                new QWebChannel(qt.webChannelTransport, function(channel) {
                    var handler = channel.objects.handler;
                    handler.handleElementClick(html, xpath); // 通过QWebChannel将HTML传递给Qt的handler对象处理
                });
                removeEventListener();      // 取消绑定事件
                enableLinksAndButtons();    // 启用链接和按钮的默认行为
            }

            // 获取元素的 XPath 路径
            function getXPath(element) {
                if (element.id !== "") { // 如果元素具有 ID 属性
                    return '//*[@id="' + element.id + '"]'; // 返回格式为 '//*[@id="elementId"]' 的 XPath 路径
                }
                if (element === document.body) { // 如果当前元素是 document.body
                    return "/html/body"; // 返回 '/html/body' 的 XPath 路径
                }
                
                var index = 1;
                const childNodes = element.parentNode ? element.parentNode.childNodes : []; // 获取当前元素的父节点的子节点列表
                var siblings = childNodes;
                
                for (var i = 0; i < siblings.length; i++) {
                    var sibling = siblings[i];
                    if (sibling === element) { // 遍历到当前元素
                    // 递归调用，获取父节点的 XPath 路径，然后拼接当前元素的标签名和索引
                    return (
                        getXPath(element.parentNode) +
                        "/" +
                        element.tagName.toLowerCase() +
                        "[" +
                        index +
                        "]"
                    );
                    }
                    if (sibling.nodeType === 1 && sibling.tagName === element.tagName) { // 遍历到具有相同标签名的元素
                    index++; // 增加索引值
                    }
                }
            }

            // 取消绑定事件
            function removeEventListener(){
                document.removeEventListener('mouseover', mouseoverEvent);
                document.removeEventListener('mouseout', mouseoutEvent);
                document.removeEventListener('click', clickEvent);
            }

            // 禁用链接和按钮的默认行为
            function disableLinksAndButtons() {
                var links = document.getElementsByTagName('a');
                for (var i = 0; i < links.length; i++) {
                    links[i].onclick = function(event) {
                        event.preventDefault(); // 阻止链接的默认行为
                    };
                }

                var buttons = document.getElementsByTagName('button');
                for (var j = 0; j < buttons.length; j++) {
                    buttons[j].onclick = function(event) {
                        event.preventDefault(); // 阻止按钮的默认行为
                    };
                }
            }

            // 启用链接和按钮的默认行为
            function enableLinksAndButtons() {
                var links = document.getElementsByTagName('a');
                for (var i = 0; i < links.length; i++) {
                    links[i].onclick = null; // 取消阻止链接的默认行为
                }

                var buttons = document.getElementsByTagName('button');
                for (var j = 0; j < buttons.length; j++) {
                    buttons[j].onclick = null; // 取消阻止按钮的默认行为
                }
            }
        '''
        # 执行JavaScript脚本
        self.ui.webEngineView.page().runJavaScript(js_script)

    def __check_link_open_status(self):
        """ 检查链接打开状态，如果链接打开则运行选择元素，未打开则弹窗 """
        if not self.link_open_status:
            message_box("open url", "你还没有打开网站")
            self.logger.warning("未打开网站")
        else:
            self.__select_element()

    def get_xpath(self, element):
        """ 获取自定义xpath """
        self.selectElement = element
        xpath, ok = QInputDialog.getText(self, self.element[self.selectElement][2], '请输入XPath:')
        if ok:
            self.element[self.selectElement][3] = xpath
            self.logger.info(f"输入{self.element[self.selectElement][2]}的XPath: {xpath}")
        self.__update_config_label()

if __name__ == "__main__":
    app = QApplication([])

    window = Main()
    window.show()

    sys.exit(app.exec())