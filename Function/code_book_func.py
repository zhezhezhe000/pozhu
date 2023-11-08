import sys, os
import pyperclip    # 剪贴板操作库
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog
from collections import OrderedDict # 保证顺序去重

from UI.code_book_ui import Ui_Form    # 导入对应UI文件

class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dir_path = "./Dict/"
        self.dict_list = []
        # 调用逻辑方法
        self._logic_func()

    """
    内部方法
    """

    def _logic_func(self):
        """ 内容设置 """
        # 设置下拉框内容
        self.__comboBox_addItems()
        # 禁用下拉框鼠标滚轮选中
        self.comboBox.wheelEvent = self.__prevent_wheel_event

        """ 绑定信号方法 """
        # 粘贴
        self.pushButton_paste.clicked.connect(self.__paste_func)
        # 加载
        self.pushButton_load.clicked.connect(self.__load_func)
        # 移除
        self.pushButton_remove.clicked.connect(self.__remove_func)
        # 清除：ui代码中已经绑定该功能，这里覆写添加新功能
        self.pushButton_clear.clicked.connect(self.__clear_func)
        # 添加
        self.pushButton_add.clicked.connect(self.__add_func)
        # 回车添加
        self.lineEdit.returnPressed.connect(self.__add_func)
        # 设置下拉框选中后的操作
        self.comboBox.currentIndexChanged.connect(self.__set_dict_func)

    def __comboBox_addItems(self):
        """ 添加下拉框内容 """
        self.dict_list = self.__get_txt_path()
        for i in self.dict_list:
            self.comboBox.addItem(i[0])
        

    def __paste_func(self):
        """ 从剪贴板粘贴到列表 """
        # 读取剪贴板
        clipboard_data = pyperclip.paste().split("\r\n")
        # 将剪贴板的数据写入列表
        self.__add_list_item(clipboard_data)

    def __load_func(self):
        """ 从文件加载到列表 """
        options = QFileDialog.Options()
        # 打开文件
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "",
            "All Files (*);;Text Files (*.txt)", 
            options=options
        )
        # 读取文件
        self.__add_to_list_from_file(file_name)

    def __remove_func(self):
        """ 移除列表选中项 """
        # 获取选中的项
        selected_items = self.listWidget.selectedItems()
        # 遍历选中的项
        for item in selected_items:
            # 移除列表项
            self.listWidget.takeItem(self.listWidget.row(item))
        self.__update_lable()

    def __clear_func(self):
        self.listWidget.clear()
        self.__update_lable()

    def __add_func(self):
        """ 添加列表项 """
        # 获取输入框内容
        input_text = self.lineEdit.text()
        # 判断输入框内容是否为空
        if input_text:
            # 添加到列表
            self.listWidget.addItem(input_text)
            # 清空输入框
            self.lineEdit.clear()
        self.__update_lable()

    def __set_dict_func(self):
        """ 设置选中下拉框后将其对应的文件导入列表 """
        # 获取选中的下拉框项
        selected_item = self.comboBox.currentText()
        # 判断选中项是否为空，且不能是第一个默认项（即第0号元素）
        if selected_item and self.comboBox.currentIndex():
            # 遍历字典列表，获取匹配项的路径
            for filename, path in self.dict_list:
                if selected_item == filename:
                    # 添加文件到列表
                    self.__add_to_list_from_file(path)

    """ 
    内部方法-公共函数 
    """

    def __add_list_item(self, items:list):
        """ 批量添加列表项 """
        items = [item.replace("\n", "").replace("\r", "") for item in items]
        self.listWidget.addItems(items)
        self.__update_lable()

    def __update_lable(self):
        """ 保证顺序进行去重 """
        unique_items = list(OrderedDict.fromkeys(self.get_all_items()))
        self.listWidget.clear()
        self.listWidget.addItems(unique_items)
        
        """ 更新标签 """
        self.label.setText(f"当前字典数量【去重后】：{self.listWidget.count()}")
        

    def __get_txt_path(self):
        """ 获取指定目录下所有txt文件文件名和路径 """
        # 如果指定文件夹不存在则创建文件夹
        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)
        # 获取当前目录下所有txt文件
        files = os.listdir(self.dir_path)
        # 获取txt文件名和路径
        file_list = [(file.replace(".txt", ""), os.path.join(self.dir_path, file)) for file in files if file.endswith(".txt")]
        return file_list
    
    def __add_to_list_from_file(self, file_name):
        """ 从指定目录下txt文件中读取内容并添加到列表中 """
        try:
            with open(file_name, "r") as f:
                # 读取文件内容
                file_data = f.readlines()
                self.__add_list_item(file_data)
        except UnicodeDecodeError:
            with open(file_name, "r", encoding='utf8') as f:
                # 读取文件内容
                file_data = f.readlines()
                self.__add_list_item(file_data)
        except FileNotFoundError:
            pass


    def __prevent_wheel_event(self, event):
        """ 禁用鼠标滚轮滚动选中 """
        event.ignore()

    """
    外部方法
    """
    def get_all_items(self):
        """ 获取所有列表项 """
        items = [item.text() for item in self.listWidget.findItems("*", Qt.MatchWildcard)]
        return items
    


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec())