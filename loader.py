import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile,QTimer,QIODevice

from ui.compiled_resource import *

'''启动加载页面'''
class Loader(QMainWindow):
    def __init__(self,main_app,load_time):
        super().__init__()
        
        #设置加载速度 +1 需要的时间 
        self.loadtk = load_time
        # 动态加载ui文件
        ui_file_name = "./ui/loading.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)

        # 从UI定义中 创建一个相应的窗口对象
        self.loaderUi = QUiLoader().load(ui_file)

        # 链接组件，加载触发
        self.loaderUi.cancelButton.clicked.connect(self.handleCancel)
        self.loaderUi.pauseButton.clicked.connect(self.handlePause)
        # 设置初始启动位置
        self.loaderUi.setGeometry(100, 100, 800, 600)
        #self.loaderUi.loadProgressBar.connect(self.handleProgressBar)

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
        if(self.is_stop == False):
            self.is_stop = True
            self.loaderUi.pauseButton.setText("继续")
            self.timer.stop()

        # 如果正在暂停中，那么继续加载
        elif(self.is_stop == True):
            self.is_stop = False
            self.timer.start(self.loadtk)
            self.loaderUi.pauseButton.setText("暂停")
    def init_ui(self):
        # 设置定时器，模拟加载过程
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handleProgressBar)
        self.timer.start(self.loadtk)

        #打开画面

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

