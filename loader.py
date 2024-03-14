import sys

from PySide6.QtWidgets import QMainWindow,QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer
from PySide6.QtGui import Qt
from ui.compiled_resource import *

'''启动加载页面'''


class Loader(QMainWindow,QDialog):
    def __init__(self, parent=None, main_app=None, load_time=100):
        super().__init__(parent)
        
        self.set_window()
        # 设置加载速度 +1 需要的时间
        self.loadtk = load_time


        loader = QUiLoader()

        # 动态加载ui文件
        ui_file_name = "./ui/loading.ui"
        ui_file = QFile(ui_file_name)
        ui_file.open(QFile.ReadOnly)

        # 从UI定义中 创建一个相应的窗口对象
        self.loaderUi = loader.load(ui_file)
        ui_file.close()

        # 链接组件，加载触发
        self.loaderUi.cancelButton.clicked.connect(self.handleCancel)
        self.loaderUi.pauseButton.clicked.connect(self.handlePause)
        # 设置初始启动位置
        self.loaderUi.setGeometry(100, 100, 800, 600)
        # self.loaderUi.loadProgressBar.connect(self.handleProgressBar)

        # 主任务
        self.main_app = main_app
        self.init_ui()

        # 暂停标志
        self.is_stop = False

    def handleCancel(self):
        # 如果取消，直接关闭程序
        sys.exit(0)

    def handlePause(self):
        # 如果没有暂停，那么暂停
        if (self.is_stop == False):
            self.is_stop = True
            self.loaderUi.pauseButton.setText("继续")
            self.timer.stop()

        # 如果正在暂停中，那么继续加载
        elif (self.is_stop == True):
            self.is_stop = False
            self.timer.start(self.loadtk)
            self.loaderUi.pauseButton.setText("暂停")

    def init_ui(self):
        # 设置定时器，模拟加载过程
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handleProgressBar)
        self.timer.start(self.loadtk)

        # 打开加载画面
        self.loaderUi.show()

    def handleProgressBar(self):
        # 模拟加载过程，每次增加一定的进度
        value = self.loaderUi.loadProgressBar.value() + 1
        self.loaderUi.loadProgressBar.setValue(value)

        if value >= 100:
            # 加载完成后关闭加载页面，并显示主窗口
            self.timer.stop()
            self.loaderUi.close()
            self.main_app.show()

    def set_window(self):
       # 关闭系统标题栏
       self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint
                           | Qt.WindowMaximizeButtonHint)
       # 透明背景
       self.setAttribute(Qt.WA_TranslucentBackground)