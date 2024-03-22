# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        if not LoadingScreen.objectName():
            LoadingScreen.setObjectName(u"LoadingScreen")
        LoadingScreen.resize(791, 622)
        LoadingScreen.setMinimumSize(QSize(620, 0))
        LoadingScreen.setProperty("unifiedTitleAndToolBarOnMac", False)
        self.horizontalLayout = QHBoxLayout(LoadingScreen)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(LoadingScreen)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"\n"
"border-image: url(:/loader/resource/background.jpg);")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(LoadingScreen)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(LoadingScreen)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(7)
        self.groupBox.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ProgramComboBox = QComboBox(self.groupBox)
        self.ProgramComboBox.addItem("")
        self.ProgramComboBox.addItem("")
        self.ProgramComboBox.addItem("")
        self.ProgramComboBox.setObjectName(u"ProgramComboBox")
        font1 = QFont()
        font1.setPointSize(7)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.ProgramComboBox.setFont(font1)
        self.ProgramComboBox.setMaxVisibleItems(11)

        self.verticalLayout_5.addWidget(self.ProgramComboBox)

        self.startButton = QPushButton(self.groupBox)
        self.startButton.setObjectName(u"startButton")

        self.verticalLayout_5.addWidget(self.startButton)

        self.stopButton = QPushButton(self.groupBox)
        self.stopButton.setObjectName(u"stopButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.stopButton)

        self.exitButton = QPushButton(self.groupBox)
        self.exitButton.setObjectName(u"exitButton")

        self.verticalLayout_5.addWidget(self.exitButton)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.debugBrowser = QTextBrowser(LoadingScreen)
        self.debugBrowser.setObjectName(u"debugBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.debugBrowser.sizePolicy().hasHeightForWidth())
        self.debugBrowser.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.debugBrowser)

        self.loadProgressBar = QProgressBar(LoadingScreen)
        self.loadProgressBar.setObjectName(u"loadProgressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.loadProgressBar.sizePolicy().hasHeightForWidth())
        self.loadProgressBar.setSizePolicy(sizePolicy3)
        self.loadProgressBar.setValue(0)
        self.loadProgressBar.setTextVisible(False)
        self.loadProgressBar.setOrientation(Qt.Horizontal)
        self.loadProgressBar.setInvertedAppearance(False)
        self.loadProgressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_2.addWidget(self.loadProgressBar)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_4.setStretch(0, 6)
        self.verticalLayout_4.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(LoadingScreen)

        QMetaObject.connectSlotsByName(LoadingScreen)
    # setupUi

    def retranslateUi(self, LoadingScreen):
        LoadingScreen.setWindowTitle(QCoreApplication.translate("LoadingScreen", u"LoadingScreen", None))
        self.label.setText(QCoreApplication.translate("LoadingScreen", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoadingScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">\u6d4b\u8bd5\u7cfb\u7edf</span></p></body></html>", None))
        self.groupBox.setTitle("")
        self.ProgramComboBox.setItemText(0, QCoreApplication.translate("LoadingScreen", u"\u9879\u76ee\u9009\u62e9", None))
        self.ProgramComboBox.setItemText(1, QCoreApplication.translate("LoadingScreen", u"\u53cd\u65e0\u4eba\u673a", None))
        self.ProgramComboBox.setItemText(2, QCoreApplication.translate("LoadingScreen", u"\u5e76\u8054\u673a\u5668\u4eba", None))

        self.ProgramComboBox.setCurrentText(QCoreApplication.translate("LoadingScreen", u"\u9879\u76ee\u9009\u62e9", None))
        self.startButton.setText(QCoreApplication.translate("LoadingScreen", u"\u542f\u52a8", None))
        self.stopButton.setText(QCoreApplication.translate("LoadingScreen", u"\u505c\u6b62", None))
        self.exitButton.setText(QCoreApplication.translate("LoadingScreen", u"\u9000\u51fa", None))
    # retranslateUi

