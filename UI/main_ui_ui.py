# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTextBrowser, QToolBox,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1099, 805)
        icon = QIcon()
        icon.addFile(u":/icon/bamboo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_target = QLineEdit(self.widget)
        self.lineEdit_target.setObjectName(u"lineEdit_target")

        self.horizontalLayout.addWidget(self.lineEdit_target)

        self.pushButton_open = QPushButton(self.widget)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.pushButton_start = QPushButton(self.widget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setEnabled(True)

        self.horizontalLayout.addWidget(self.pushButton_start)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 1)

        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout_5.addWidget(self.webEngineView, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 280))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.widget_2)
        self.toolBox.setObjectName(u"toolBox")
        self.page_optionSetting = QWidget()
        self.page_optionSetting.setObjectName(u"page_optionSetting")
        self.page_optionSetting.setGeometry(QRect(0, 0, 439, 220))
        self.gridLayout = QGridLayout(self.page_optionSetting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_5 = QWidget(self.page_optionSetting)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.doubleSpinBox_timeout = QDoubleSpinBox(self.widget_5)
        self.doubleSpinBox_timeout.setObjectName(u"doubleSpinBox_timeout")
        self.doubleSpinBox_timeout.setSingleStep(1.000000000000000)
        self.doubleSpinBox_timeout.setValue(10.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_timeout, 3, 1, 1, 1)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.checkBox_proxy = QCheckBox(self.widget_5)
        self.checkBox_proxy.setObjectName(u"checkBox_proxy")

        self.gridLayout_4.addWidget(self.checkBox_proxy, 7, 0, 1, 1)

        self.checkBox_screenshot = QCheckBox(self.widget_5)
        self.checkBox_screenshot.setObjectName(u"checkBox_screenshot")
        self.checkBox_screenshot.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_screenshot, 7, 1, 1, 1)

        self.doubleSpinBox_delay = QDoubleSpinBox(self.widget_5)
        self.doubleSpinBox_delay.setObjectName(u"doubleSpinBox_delay")
        self.doubleSpinBox_delay.setValue(0.200000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_delay, 4, 1, 1, 1)

        self.spinBox_thread = QSpinBox(self.widget_5)
        self.spinBox_thread.setObjectName(u"spinBox_thread")
        self.spinBox_thread.setMinimum(1)
        self.spinBox_thread.setMaximum(10)
        self.spinBox_thread.setValue(3)

        self.gridLayout_4.addWidget(self.spinBox_thread, 5, 1, 1, 1)

        self.comboBox_blast = QComboBox(self.widget_5)
        self.comboBox_blast.addItem("")
        self.comboBox_blast.addItem("")
        self.comboBox_blast.addItem("")
        self.comboBox_blast.addItem("")
        self.comboBox_blast.setObjectName(u"comboBox_blast")

        self.gridLayout_4.addWidget(self.comboBox_blast, 0, 1, 1, 2)

        self.label_des = QLabel(self.widget_5)
        self.label_des.setObjectName(u"label_des")

        self.gridLayout_4.addWidget(self.label_des, 1, 0, 1, 3)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 5, 0, 1, 1)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 8, 0, 1, 1)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 1)

        self.lineEdit_proxy = QLineEdit(self.widget_5)
        self.lineEdit_proxy.setObjectName(u"lineEdit_proxy")
        self.lineEdit_proxy.setEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_proxy, 8, 1, 1, 2)

        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 6, 0, 1, 1)

        self.spinBox_retryNum = QSpinBox(self.widget_5)
        self.spinBox_retryNum.setObjectName(u"spinBox_retryNum")
        self.spinBox_retryNum.setEnabled(True)
        self.spinBox_retryNum.setMinimum(1)
        self.spinBox_retryNum.setMaximum(10)
        self.spinBox_retryNum.setValue(2)

        self.gridLayout_4.addWidget(self.spinBox_retryNum, 6, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_optionSetting, u"\u53c2\u6570\u8bbe\u7f6e")
        self.page_elementSelect = QWidget()
        self.page_elementSelect.setObjectName(u"page_elementSelect")
        self.page_elementSelect.setGeometry(QRect(0, 0, 439, 220))
        self.gridLayout_6 = QGridLayout(self.page_elementSelect)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame = QFrame(self.page_elementSelect)
        self.frame.setObjectName(u"frame")
        self.frame.setMouseTracking(False)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_standby = QCheckBox(self.frame)
        self.checkBox_standby.setObjectName(u"checkBox_standby")

        self.horizontalLayout_4.addWidget(self.checkBox_standby)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_select = QComboBox(self.frame)
        self.comboBox_select.addItem("")
        self.comboBox_select.addItem("")
        self.comboBox_select.addItem("")
        self.comboBox_select.setObjectName(u"comboBox_select")
        self.comboBox_select.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.comboBox_select)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 5)

        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.pushButton_selectUser = QPushButton(self.frame)
        self.pushButton_selectUser.setObjectName(u"pushButton_selectUser")

        self.gridLayout_3.addWidget(self.pushButton_selectUser, 1, 0, 1, 1)

        self.pushButton_selectPass = QPushButton(self.frame)
        self.pushButton_selectPass.setObjectName(u"pushButton_selectPass")

        self.gridLayout_3.addWidget(self.pushButton_selectPass, 2, 0, 1, 1)

        self.pushButton_selectCode = QPushButton(self.frame)
        self.pushButton_selectCode.setObjectName(u"pushButton_selectCode")
        self.pushButton_selectCode.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButton_selectCode, 3, 0, 1, 1)

        self.pushButton_selectCodeInput = QPushButton(self.frame)
        self.pushButton_selectCodeInput.setObjectName(u"pushButton_selectCodeInput")
        self.pushButton_selectCodeInput.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButton_selectCodeInput, 4, 0, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)

        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)

        self.lineEdit_codeInputError = QLineEdit(self.frame)
        self.lineEdit_codeInputError.setObjectName(u"lineEdit_codeInputError")
        self.lineEdit_codeInputError.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_codeInputError, 6, 0, 1, 1)

        self.pushButton_selectLogin = QPushButton(self.frame)
        self.pushButton_selectLogin.setObjectName(u"pushButton_selectLogin")

        self.gridLayout_3.addWidget(self.pushButton_selectLogin, 7, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_elementSelect, u"\u5143\u7d20\u9009\u62e9")

        self.horizontalLayout_2.addWidget(self.toolBox)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_config = QTextBrowser(self.widget_4)
        self.textBrowser_config.setObjectName(u"textBrowser_config")

        self.gridLayout_2.addWidget(self.textBrowser_config, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 3)

        self.gridLayout_5.addWidget(self.widget_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1099, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_target, self.pushButton_open)
        QWidget.setTabOrder(self.pushButton_open, self.pushButton_start)
        QWidget.setTabOrder(self.pushButton_start, self.tabWidget)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionabout)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7834\u7af9v1.5      by\uff1a\u8ff7\u8ff7\u60d8\u60d8\uff08\u4e25\u7981\u7528\u4e8e\u975e\u6388\u6743\u4f7f\u7528\u53ca\u975e\u6cd5\u6d4b\u8bd5\u7528\u9014\uff01\uff09\u3010\u5185\u90e8\u4f7f\u7528\uff0c\u5207\u52ff\u5916\u4f20\u3011", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.lineEdit_target.setText(QCoreApplication.translate("MainWindow", u"http://127.0.0.1:5000/", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u7f51\u7ad9", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u7206\u7834", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7206\u7834\u6a21\u5f0f\uff1a", None))
        self.checkBox_proxy.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\u4ee3\u7406", None))
        self.checkBox_screenshot.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5f00\u542f\u622a\u56fe", None))
        self.comboBox_blast.setItemText(0, QCoreApplication.translate("MainWindow", u"Cluster bomb:\u96c6\u675f\u70b8\u5f39\uff08\u9ed8\u8ba4\uff09", None))
        self.comboBox_blast.setItemText(1, QCoreApplication.translate("MainWindow", u"Sinper:\u72d9\u51fb\u624b\uff08\u63a8\u8350\u5355\u5bc6\u7801\u4f7f\u7528\uff09", None))
        self.comboBox_blast.setItemText(2, QCoreApplication.translate("MainWindow", u"Battering ram:\u653b\u57ce\u9524", None))
        self.comboBox_blast.setItemText(3, QCoreApplication.translate("MainWindow", u"Pitchfork:\u8349\u53c9\u6a21\u5f0f", None))

        self.label_des.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\u8bf4\u660e\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u6c42\u5ef6\u65f6(s)\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b\u8bbe\u7f6e\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u5730\u5740\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u65f6\u65f6\u95f4(s)\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u7801\u8f93\u5165\u9519\u8bef\u91cd\u8bd5\u6570\uff1a", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_optionSetting), QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.checkBox_standby.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\u5907\u7528\u6a21\u5f0f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6a21\u5f0f\uff1a", None))
        self.comboBox_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\uff1a\u8d26\u53f7\u3001\u5bc6\u7801", None))
        self.comboBox_select.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5355\u5bc6\u7801", None))
        self.comboBox_select.setItemText(2, QCoreApplication.translate("MainWindow", u"\u8d26\u53f7\u3001\u5bc6\u7801\u3001\u9a8c\u8bc1\u7801", None))

        self.pushButton_selectUser.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d\u5143\u7d20\u9009\u62e9", None))
        self.pushButton_selectPass.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\u5143\u7d20\u9009\u62e9", None))
        self.pushButton_selectCode.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u7801\u5143\u7d20\u9009\u62e9", None))
        self.pushButton_selectCodeInput.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u7801\u8f93\u5165\u9009\u62e9", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u7801\u9519\u8bef\u63d0\u793a\uff08\u4e3a\u7a7a\u5219\u4e0d\u8fdb\u884c\u6821\u9a8c\uff09\uff1a", None))
        self.pushButton_selectLogin.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u6309\u94ae\u9009\u62e9", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_elementSelect), QCoreApplication.translate("MainWindow", u"\u5143\u7d20\u9009\u62e9", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e\u5185\u5bb9\uff1a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

