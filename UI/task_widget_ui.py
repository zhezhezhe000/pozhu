# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

from UI.CodeEditor import CodeEditor
from UI.ImageViewer import ImageViewer

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(744, 593)
        Dialog.setModal(False)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 3, 1, 1, 1)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_request = QWidget()
        self.tab_request.setObjectName(u"tab_request")
        self.gridLayout_2 = QGridLayout(self.tab_request)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit_html = CodeEditor(self.tab_request)
        self.plainTextEdit_html.setObjectName(u"plainTextEdit_html")

        self.gridLayout_2.addWidget(self.plainTextEdit_html, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_request, "")
        self.tab_screenshot = QWidget()
        self.tab_screenshot.setObjectName(u"tab_screenshot")
        self.gridLayout_4 = QGridLayout(self.tab_screenshot)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea = ImageViewer(self.tab_screenshot)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 98, 28))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_9)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_screenshot, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_config = QPushButton(self.widget)
        self.pushButton_config.setObjectName(u"pushButton_config")

        self.horizontalLayout.addWidget(self.pushButton_config)

        self.pushButton_pause = QPushButton(self.widget)
        self.pushButton_pause.setObjectName(u"pushButton_pause")

        self.horizontalLayout.addWidget(self.pushButton_pause)

        self.pushButton_stop = QPushButton(self.widget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.horizontalSpacer = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_request), QCoreApplication.translate("Dialog", u"page_html\uff1a\u9875\u9762html\u4ee3\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_screenshot), QCoreApplication.translate("Dialog", u"screenshot:\u622a\u56fe", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8fd0\u884c\u4e2d", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Request", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Username", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Password", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Timeout", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Length", None));
        self.pushButton_config.setText(QCoreApplication.translate("Dialog", u"\u67e5\u770b\u53c2\u6570\u914d\u7f6e", None))
        self.pushButton_pause.setText(QCoreApplication.translate("Dialog", u"\u6682\u505c\u4efb\u52a1", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Dialog", u"\u7ec8\u6b62\u4efb\u52a1", None))
    # retranslateUi

