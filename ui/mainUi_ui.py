# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUi.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.actionchose_input = QAction(MainWindow)
        self.actionchose_input.setObjectName(u"actionchose_input")
        self.verticalLayout_4 = QVBoxLayout(MainWindow)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_label = QLabel(MainWindow)
        self.frame_label.setObjectName(u"frame_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label.sizePolicy().hasHeightForWidth())
        self.frame_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.frame_label)

        self.line = QFrame(MainWindow)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.debug_msg = QTextBrowser(MainWindow)
        self.debug_msg.setObjectName(u"debug_msg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.debug_msg.sizePolicy().hasHeightForWidth())
        self.debug_msg.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.debug_msg)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_sw = QComboBox(MainWindow)
        icon = QIcon(QIcon.fromTheme(u"camera-video"))
        self.frame_sw.addItem(icon, "")
        self.frame_sw.addItem("")
        self.frame_sw.addItem("")
        self.frame_sw.addItem("")
        self.frame_sw.setObjectName(u"frame_sw")

        self.gridLayout_2.addWidget(self.frame_sw, 1, 0, 1, 1)

        self.start_btn = QPushButton(MainWindow)
        self.start_btn.setObjectName(u"start_btn")

        self.gridLayout_2.addWidget(self.start_btn, 0, 0, 1, 1)

        self.stop_btn = QPushButton(MainWindow)
        self.stop_btn.setObjectName(u"stop_btn")

        self.gridLayout_2.addWidget(self.stop_btn, 0, 1, 1, 1)

        self.mode_sw = QComboBox(MainWindow)
        icon1 = QIcon(QIcon.fromTheme(u"preferences"))
        self.mode_sw.addItem(icon1, "")
        self.mode_sw.addItem("")
        self.mode_sw.addItem("")
        self.mode_sw.addItem("")
        self.mode_sw.setObjectName(u"mode_sw")

        self.gridLayout_2.addWidget(self.mode_sw, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        self.verticalLayout_4.addWidget(self.statusbar)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionchose_input.setText(QCoreApplication.translate("MainWindow", u"chose input", None))
        self.frame_label.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u663e\u793a", None))
        self.debug_msg.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'UbuntuMono Nerd Font'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.frame_sw.setItemText(0, QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u8f93\u5165", None))
        self.frame_sw.setItemText(1, QCoreApplication.translate("MainWindow", u"socket", None))
        self.frame_sw.setItemText(2, QCoreApplication.translate("MainWindow", u"video", None))
        self.frame_sw.setItemText(3, QCoreApplication.translate("MainWindow", u"local", None))

        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Debug\u542f\u52a8", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"debug\u505c\u6b62", None))
        self.mode_sw.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\u9009\u62e9", None))
        self.mode_sw.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5de1\u822a\u6a21\u5f0f", None))
        self.mode_sw.setItemText(2, QCoreApplication.translate("MainWindow", u"\u8ddf\u8e2a\u6a21\u5f0f", None))
        self.mode_sw.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5f00\u706b\u6a21\u5f0f", None))

    # retranslateUi

