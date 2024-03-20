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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        if not LoadingScreen.objectName():
            LoadingScreen.setObjectName(u"LoadingScreen")
        LoadingScreen.resize(620, 480)
        LoadingScreen.setMinimumSize(QSize(620, 0))
        LoadingScreen.setProperty("unifiedTitleAndToolBarOnMac", False)
        self.verticalLayout_3 = QVBoxLayout(LoadingScreen)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(LoadingScreen)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.loadProgressBar = QProgressBar(LoadingScreen)
        self.loadProgressBar.setObjectName(u"loadProgressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loadProgressBar.sizePolicy().hasHeightForWidth())
        self.loadProgressBar.setSizePolicy(sizePolicy1)
        self.loadProgressBar.setValue(0)

        self.verticalLayout.addWidget(self.loadProgressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.startButton = QPushButton(LoadingScreen)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout.addWidget(self.startButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pauseButton = QPushButton(LoadingScreen)
        self.pauseButton.setObjectName(u"pauseButton")

        self.horizontalLayout.addWidget(self.pauseButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.resumeButton = QPushButton(LoadingScreen)
        self.resumeButton.setObjectName(u"resumeButton")

        self.horizontalLayout.addWidget(self.resumeButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stopButton = QPushButton(LoadingScreen)
        self.stopButton.setObjectName(u"stopButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.stopButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.statusbar = QStatusBar(LoadingScreen)
        self.statusbar.setObjectName(u"statusbar")

        self.verticalLayout_3.addWidget(self.statusbar)


        self.retranslateUi(LoadingScreen)

        QMetaObject.connectSlotsByName(LoadingScreen)
    # setupUi

    def retranslateUi(self, LoadingScreen):
        LoadingScreen.setWindowTitle(QCoreApplication.translate("LoadingScreen", u"LoadingScreen", None))
        self.label.setText(QCoreApplication.translate("LoadingScreen", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoadingScreen", u"\u53cd\u65e0\u4eba\u53ca\u6d4b\u8bd5\u7cfb\u7edf", None))
        self.startButton.setText(QCoreApplication.translate("LoadingScreen", u"\u542f\u52a8", None))
        self.pauseButton.setText(QCoreApplication.translate("LoadingScreen", u"\u6682\u505c", None))
        self.resumeButton.setText(QCoreApplication.translate("LoadingScreen", u"\u6062\u590d", None))
        self.stopButton.setText(QCoreApplication.translate("LoadingScreen", u"\u505c\u6b62", None))
    # retranslateUi

