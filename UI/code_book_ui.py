# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'code_book.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(344, 211)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_paste = QPushButton(Form)
        self.pushButton_paste.setObjectName(u"pushButton_paste")

        self.gridLayout.addWidget(self.pushButton_paste, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 2)

        self.pushButton_load = QPushButton(Form)
        self.pushButton_load.setObjectName(u"pushButton_load")

        self.gridLayout.addWidget(self.pushButton_load, 1, 0, 1, 1)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 6, 0, 1, 2)

        self.pushButton_remove = QPushButton(Form)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.gridLayout.addWidget(self.pushButton_remove, 2, 0, 1, 1)

        self.pushButton_add = QPushButton(Form)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.gridLayout.addWidget(self.pushButton_add, 4, 0, 1, 1)

        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.gridLayout.addWidget(self.pushButton_clear, 3, 0, 1, 1)

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"alternate-background-color:lightgray;\n"
"")
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayout.addWidget(self.listWidget, 0, 1, 4, 1)


        self.retranslateUi(Form)
        self.pushButton_clear.clicked.connect(self.listWidget.clear)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_paste.setText(QCoreApplication.translate("Form", u"Paste:\u7c98\u8d34", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u5b57\u5178\u6570\u91cf\uff1a0", None))
        self.pushButton_load.setText(QCoreApplication.translate("Form", u"Load...:\u52a0\u8f7d", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u4ece\u5217\u8868\u6dfb\u52a0...", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"\u4ece\u5217\u8868\u6dfb\u52a0...", None))
        self.pushButton_remove.setText(QCoreApplication.translate("Form", u"Remove:\u79fb\u9664", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"Add:\u6dfb\u52a0", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"Clear:\u6e05\u7a7a", None))
    # retranslateUi

