import sys
from PySide6.QtWidgets import QApplication, QLabel, QScrollArea, QWidget, QSizePolicy
from PySide6.QtGui import QPixmap, QPalette
from PySide6.QtCore import Qt

class ImageViewer(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 获取滚动区域默认的滚动事件
        self.scroll_wheelEvent = self.wheelEvent
        self.setImage()
        # 启用垂直和水平滚动条
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # 设置滚动组件样式
        self.setBackgroundRole(QPalette.Dark)
        
    def setImage(self, image_path=None):
        """ 设置图像 """
        # 创建一个用于显示图像的标签
        removed_widget = self.takeWidget()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # 标签位于左上角
        if image_path is None:
            self.image_label.setText("无截图")
        else:
            self.image_label.setScaledContents(True)  # 允许调整大小
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap)
            else:
                self.image_label.setText("图片加载失败，请查看截图目录！")
        self.setWidget(self.image_label)
        

    def keyPressEvent(self, event):
        """ 键盘按下事件 """
        key = event.key()
        if key == 16777249:
            self.wheelEvent = self.new_wheelEvent
        # print(f"Key pressed: {key}",type(key))

    def keyReleaseEvent(self, event):
        """ 键盘抬起事件 """
        key = event.key()
        if key == 16777249:
            self.wheelEvent = self.scroll_wheelEvent
        # print(f"Key released: {key}",event,event.type()) 

    def new_wheelEvent(self, event):
        """鼠标滚轮事件"""
        # 检查是否按下Ctrl键
        if event.modifiers() == Qt.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                # 放大图像
                self.zoomImage(1.1)
            else:
                # 缩小图像
                self.zoomImage(0.9)

    def zoomImage(self, factor):
        """缩放图像"""
        # 获取当前标签大小
        label_size = self.image_label.size()

        # 计算新大小
        new_size = label_size * factor
        # print(factor, label_size, new_size)
        if new_size.width() < 20 or new_size.height() < 20:
            # 防止缩小太小
            return

        # 设置新大小
        """
        一个大小bug
        记录
        resize设置组件大小
        setFixedSize设置布局大小，一般都会被父组件设置布局，控件处于布局内，大小由布局控制，resize没用
        """
        self.image_label.setFixedSize(new_size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.setImage("1-a-a.png")
    viewer.setImage("111.png")
    viewer.show()
    sys.exit(app.exec())
