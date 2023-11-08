# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statement.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(498, 341)
        icon = QIcon()
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(Qt.LeftToRight)
        Dialog.setInputMethodHints(Qt.ImhNone)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u514d\u8d23\u58f0\u660e", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8bf7\u4ed4\u7ec6\u9605\u8bfb\u4ee5\u4e0b\u58f0\u660e\uff0c\u5426\u5219\u4e0d\u8981\u4f7f\u7528\u8be5\u5de5\u5177\uff0c\u60a8\u7684\u4f7f\u7528\u884c\u4e3a\u6216\u8005\u60a8\u4ee5\u5176\u4ed6\u4efb\u4f55\u65b9\u5f0f\u8868\u793a\u63a5\u53d7\u672c\u534f\u8bae\u7684\uff0c\u5373\u89c6\u4e3a\u60a8\u5df2\u9605\u8bfb\u5e76\u540c\u610f\u672c\u534f\u8bae\u7684\u7ea6\u675f\u3002</p>\n"
"<p style=\" m"
                        "argin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u514d\u8d23\u58f0\u660e\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. \u672c\u9879\u76ee\u7981\u6b62\u7528\u4e8e\u672a\u6388\u6743\u548c\u975e\u6cd5\u6d4b\u8bd5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. \u8be5\u9879\u76ee\u4e3a\u4f5c\u8005\u5b66\u4e60selenium4\u548cpyside6\u540e\u7684\u60f3\u6cd5\u4ea7\u51fa</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. \u5982\u60a8\u5728\u4f7f\u7528\u672c\u5de5\u5177\u7684\u8fc7\u7a0b\u4e2d\u5b58\u5728\u4efb\u4f55\u975e\u6cd5\u884c\u4e3a\uff0c\u60a8\u9700\u81ea\u884c\u627f\u62c5\u76f8\u5e94\u540e\u679c\uff0c\u4f5c\u8005\u4e0d\u627f\u62c5\u4efb\u4f55\u6cd5\u5f8b\u53ca\u8fde\u5e26\u8d23\u4efb</p>\n"
"<hr />\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7f51\u7edc\u5b89\u5168\u6cd5\u666e\u53ca\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7b2c\u4e8c\u5341\u4e03\u6761 \u4efb\u4f55\u4e2a\u4eba\u548c\u7ec4\u7ec7\u4e0d\u5f97\u4ece\u4e8b\u975e\u6cd5\u4fb5\u5165\u4ed6\u4eba\u7f51\u7edc\u3001\u5e72\u6270\u4ed6\u4eba\u7f51\u7edc\u6b63\u5e38\u529f\u80fd\u3001\u7a83\u53d6\u7f51\u7edc\u6570\u636e\u7b49\u5371\u5bb3\u7f51\u7edc\u5b89\u5168\u7684\u6d3b\u52a8\uff1b\u4e0d\u5f97\u63d0\u4f9b\u4e13\u95e8\u7528\u4e8e\u4ece\u4e8b\u4fb5\u5165\u7f51\u7edc\u3001\u5e72\u6270\u7f51\u7edc\u6b63\u5e38\u529f\u80fd\u53ca\u4fdd\u62a4\u63aa\u65bd\u3001\u7a83\u53d6\u7f51\u7edc\u6570\u636e\u7b49\u5371\u5bb3\u7f51\u7edc\u5b89\u5168\u6d3b\u52a8\u7684\u7a0b\u5e8f\u3001\u5de5\u5177\uff1b\u660e\u77e5\u4ed6\u4eba\u4ece\u4e8b\u5371\u5bb3\u7f51\u7edc\u5b89\u5168\u6d3b\u52a8\u7684\uff0c\u4e0d"
                        "\u5f97\u4e3a\u5176\u63d0\u4f9b\u6280\u672f\u652f\u6301\u3001\u5e7f\u544a\u63a8\u5e7f\u3001\u652f\u4ed8\u7ed3\u7b97\u7b49\u5e2e\u52a9\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7b2c\u516d\u5341\u4e09\u6761 \u8fdd\u53cd\u672c\u6cd5\u7b2c\u4e8c\u5341\u4e03\u6761\u89c4\u5b9a\uff0c\u4ece\u4e8b\u5371\u5bb3\u7f51\u7edc\u5b89\u5168\u7684\u6d3b\u52a8\uff0c\u6216\u8005\u63d0\u4f9b\u4e13\u95e8\u7528\u4e8e\u4ece\u4e8b\u5371\u5bb3\u7f51\u7edc\u5b89\u5168\u6d3b\u52a8\u7684\u7a0b\u5e8f\u3001\u5de5\u5177\uff0c\u6216\u8005\u4e3a\u4ed6\u4eba\u4ece\u4e8b\u5371\u5bb3\u7f51\u7edc\u5b89\u5168\u7684\u6d3b\u52a8\u63d0\u4f9b\u6280\u672f\u652f\u6301\u3001\u5e7f\u544a\u63a8\u5e7f\u3001\u652f\u4ed8\u7ed3\u7b97\u7b49\u5e2e\u52a9\uff0c\u5c1a\u4e0d\u6784\u6210\u72af\u7f6a\u7684\uff0c\u7531\u516c"
                        "\u5b89\u673a\u5173\u6ca1\u6536\u8fdd\u6cd5\u6240\u5f97\uff0c\u5904\u4e94\u65e5\u4ee5\u4e0b\u62d8\u7559\uff0c\u53ef\u4ee5\u5e76\u5904\u4e94\u4e07\u5143\u4ee5\u4e0a\u4e94\u5341\u4e07\u4ee5\u4e0b\u7f5a\u6b3e\uff1b\u60c5\u8282\u8f83\u91cd\u7684\uff0c\u5904\u4e94\u65e5\u4ee5\u4e0a\u5341\u4e94\u65e5\u4ee5\u4e0b\u7f5a\u6b3e\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5355\u4f4d\u6709\u524d\u6b3e\u884c\u4e3a\u7684\uff0c\u7531\u516c\u5b89\u673a\u5173\u6ca1\u6536\u8fdd\u6cd5\u6240\u5f97\uff0c\u5904\u5341\u4e07\u5143\u4ee5\u4e0a\u4e00\u767e\u4e07\u4ee5\u4e0b\u7f5a\u6b3e\uff0c\u5e76\u5bf9\u76f4\u63a5\u8d1f\u8d23\u7684\u4e3b\u7ba1\u4eba\u5458\u548c\u5176\u4ed6\u76f4\u63a5\u8d23\u4efb\u4eba\u5458\u4f9d\u7167\u524d\u6b3e\u89c4\u5b9a\u5904\u7f5a\u3002</p>\n"
"<p style=\"-qt-pa"
                        "ragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8fdd\u53cd\u672c\u6cd5\u7b2c\u4e8c\u5341\u4e03\u6761\u89c4\u5b9a\uff0c\u53d7\u5230\u6cbb\u5b89\u7ba1\u7406\u5904\u7f5a\u7684\u4eba\u5458\uff0c\u4e94\u5e74\u5185\u4e0d\u5f97\u4ece\u4e8b\u7f51\u7edc\u5b89\u5168\u7ba1\u7406\u548c\u7f51\u7edc\u8fd0\u8425\u5173\u952e\u5c97\u4f4d\u7684\u5de5\u4f5c\uff1b\u53d7\u5230\u5211\u4e8b\u5904\u7f5a\u7684\u4eba\u5458\uff0c\u7ec8\u8eab\u4e0d\u5f97\u4ece\u4e8b\u7f51\u7edc\u5b89\u5168\u7ba1\u7406\u548c\u7f51\u7edc\u8fd0\u8425\u5173\u952e\u5c97\u4f4d\u7684\u5de5\u4f5c\u3002</p></body></html>", None))
    # retranslateUi

