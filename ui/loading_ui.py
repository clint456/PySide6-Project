# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        if not LoadingScreen.objectName():
            LoadingScreen.setObjectName(u"LoadingScreen")
        LoadingScreen.resize(620, 435)
        LoadingScreen.setMinimumSize(QSize(620, 0))
        LoadingScreen.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(LoadingScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"image: url(:/loader/resource/background.jpg);")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.loadProgressBar = QProgressBar(self.centralwidget)
        self.loadProgressBar.setObjectName(u"loadProgressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loadProgressBar.sizePolicy().hasHeightForWidth())
        self.loadProgressBar.setSizePolicy(sizePolicy1)
        self.loadProgressBar.setValue(0)

        self.verticalLayout.addWidget(self.loadProgressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pauseButton = QPushButton(self.centralwidget)
        self.pauseButton.setObjectName(u"pauseButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pauseButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        LoadingScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoadingScreen)
        self.statusbar.setObjectName(u"statusbar")
        LoadingScreen.setStatusBar(self.statusbar)

        self.retranslateUi(LoadingScreen)

        QMetaObject.connectSlotsByName(LoadingScreen)
    # setupUi

    def retranslateUi(self, LoadingScreen):
        LoadingScreen.setWindowTitle(QCoreApplication.translate("LoadingScreen", u"LoadingScreen", None))
        self.label.setText(QCoreApplication.translate("LoadingScreen", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoadingScreen", u"\u53cd\u65e0\u4eba\u53ca\u6d4b\u8bd5\u7cfb\u7edf\u6b63\u5728\u542f\u52a8\u4e2d\u2026\u2026", None))
        self.cancelButton.setText(QCoreApplication.translate("LoadingScreen", u"\u53d6\u6d88", None))
        self.pauseButton.setText(QCoreApplication.translate("LoadingScreen", u"\u6682\u505c", None))
    # retranslateUi

