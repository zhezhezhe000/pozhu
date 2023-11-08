import sys, json
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QIcon
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager    # 浏览器驱动管理器
from requests.exceptions import ConnectionError     # 请求异常连接错误
from Function import main_ui_func
from Function.static import message_box, load_config, save_config    # 公用函数
from UI.statement_ui import Ui_Dialog

# 加载json文件
config = load_config()

class Statement(QDialog, Ui_Dialog):
    """ 声明 """
    success = Signal()
    def __init__(self):
        super().__init__()
        # 初始化 UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.icon_bamboo = QIcon("icon/bamboo.png")
        self.setWindowIcon(self.icon_bamboo)

    def accept(self):
        self.success.emit()
        self.close()
    

class BrowserThread(QThread):
    """ 异步初始化加载浏览器驱动 """
    loaded = Signal(str)

    def run(self):
        status = "success"
        try:
            # 初始化浏览器驱动，自动下载相关驱动
            webdriver.chrome.service.Service(
                executable_path=ChromeDriverManager().install()
            )
        except ConnectionError:
            status = "Network Error"
        except AttributeError:
            status = "Chrome Error"
        # 发送加载完成信号
        self.loaded.emit(status)


class Main():
    def __init__(self) -> None:
        self.statement = Statement()
        self.statement.success.connect(self.run)
        

        if not config["initialize_status"]:
            message_box("初始化", "第一次运行需要初始化服务，请耐心等待！！！", QMessageBox.Information)
            # 创建异步线程并连接信号
            self.web_server_thread = BrowserThread()
            self.web_server_thread.loaded.connect(lambda status: self.__set_web_service(status))
            # 启动异步线程
            self.web_server_thread.start()
        else:
            self.statement.show()

    def __set_web_service(self, status):
        """ 设置web服务/驱动状态 """
        if status == "network error":
            message_box(status, "网络异常，请检查网络状况\n关掉代理，重启应用！", QMessageBox.Critical)
        elif status == "chrome error":
            message_box(status, "请检查一下是否安装Chrome浏览器！", QMessageBox.Critical)
        elif status == "success":
            # 设置标志位为真并保存
            config["initialize_status"] = True
            save_config(config)
            self.statement.show()


    def run(self):
        self.window = main_ui_func.Main()
        self.window.show()


if __name__ == "__main__":
    banner = f"""
                            _                          _     _      
                           | |                        | |   | |     
            _   _ _ __  ___| |_ ___  _ __  _ __   __ _| |__ | | ___ 
           | | | | '_ \/ __| __/ _ \| '_ \| '_ \ / _` | '_ \| |/ _ \\
           | |_| | | | \__ \ || (_) | |_) | |_) | (_| | |_) | |  __/
            \__,_|_| |_|___/\__\___/| .__/| .__/ \__,_|_.__/|_|\___|
                                    | |   | |                       
                                    |_|   |_|                       
     ____                 _      _______ _                           _     
    |  _ \               | |    |__   __| |                         | |    
    | |_) |_ __ ___  __ _| | __    | |  | |__  _ __ ___  _   _  __ _| |__  
    |  _ <| '__/ _ \/ _` | |/ /    | |  | '_ \| '__/ _ \| | | |/ _` | '_ \ 
    | |_) | | |  __/ (_| |   <     | |  | | | | | | (_) | |_| | (_| | | | |
    |____/|_|  \___|\__,_|_|\_\    |_|  |_| |_|_|  \___/ \__,_|\__, |_| |_|
                                                                __/ |      
                                                               |___/       
项目名：破竹
英文名： unstoppable Break Through (不可阻挡的突破)
作者：迷迷惘惘
项目地址：
版本： v{config["version"]}
声明：本项目仅用于学习和内部使用，禁止用于未授权和非法测试，保护网络安全，人人有责

"""
    print(banner)
    app = QApplication([])
    main = Main()
    sys.exit(app.exec())
