import sys
import time

from PySide6.QtCore import (QMutex, QMutexLocker, QThread, QWaitCondition,
                            Signal, Slot)
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (QApplication, QProgressBar, QPushButton,
                               QVBoxLayout, QWidget)
from qt_material import apply_stylesheet

from thr.mainWinThread import mainWinThread
from ui.loading_ui import Ui_LoadingScreen


class LoaderThread(QThread):
    """进度条加载线程"""

    valueChange = Signal(int)  # 自定义信号，用于发送进度值的变化
    loadComplete = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.progress_value = int(0)  # 设置进度条初始值
        self.is_paused = bool(0)  # 标记线程是否暂停
        self.mutex = QMutex()  # 互斥锁，用于线程同步
        self.cond = QWaitCondition()  # 设置等待条件，用于暂停和恢复

    def pause_thread(self):
        """设置线程为暂停状态"""
        with QMutexLocker(self.mutex):
            self.is_paused = True

    def resume_thread(self):
        """设置线程为非暂停状态"""
        if self.is_paused:
            with QMutexLocker(self.mutex):
                """锁定互斥锁的对象"""
                self.is_paused = False  # 设置线程为非暂停状态
                self.cond.wakeOne()  # 唤醒一个等待的线程

    def set_loadComplete(self, is_complete):
        """发送进度条加载完成"""
        self.loadComplete.emit(is_complete)

    def run(self):
        while True:
            with QMutexLocker(self.mutex):
                while self.is_paused:
                    self.cond.wait(self.mutex)  # 当线程为暂停状态时，进入等待

                if self.progress_value >= 100:
                    self.progress_value = 0
                    self.set_loadComplete(True)
                    print("================> 进度加载完成")
                    return  # 当进度条增加为100时，返回并退出线程
                else:
                    self.set_loadComplete(False)
                    self.progress_value += 1
                    self.valueChange.emit(self.progress_value)  # 发送进度条值变化
                    time.sleep(0.1)


class LoadWin(QWidget, QThread):
    # TODO 这此添加判断主页面是否加载完成的信号
    signal_show = Signal(bool)  # 用于控制主窗口显示/隐藏 默认隐藏

    def __init__(self, parent=None):
        super().__init__(parent=parent)  # 初始化父类
        self.is_show = False
        self.bar_thread_running = False  # 标记线程是否正在运行
        self.mainWin_thread_running = False
        # self.__redefine_window_border()
        self.__setup_ui()
        self.__load_connect()

    # ui界面设置
    def __redefine_window_border(self):
        """设置无边框"""
        self.setWindowFlag(
            Qt.Window
            | Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )

    def __setup_ui(self):
        """初始化designer组件"""
        self.load_ui = Ui_LoadingScreen()
        self.load_ui.setupUi(self)  # 初始化designer界面
        # 获取designer界面组件对象
        self.progress_bar = self.load_ui.loadProgressBar
        self.start_btn = self.load_ui.startButton
        self.stop_btn = self.load_ui.stopButton
        self.exit_btn = self.load_ui.exitButton
        self.debug_bw = self.load_ui.debugBrowser
        self.select_program = self.load_ui.ProgramComboBox
        self.debug_bw.setFontPointSize(11)
        self.debug_bw.setTextColor("white")

    def __load_connect(self):
        """初始化连接信号与槽"""
        self.start_btn.clicked.connect(self.start_bar_thread)
        self.stop_btn.clicked.connect(self.stop_all_thread)
        self.exit_btn.clicked.connect(self.exitProgram)
        self.select_program.activated.connect(self.changeProgram)

    def debug_msg(self, str):
        """打印信息输出到Gui面板"""
        self.debug_bw.append(str)  # 添加到面板输出流
        print(str)

    # 项目切换控制器
    @Slot(int)
    def changeProgram(self, index):
        """判断当前选择启动的项目"""
        mode = self.select_program.itemText(index)
        """判断当前系统运行模式"""
        if mode == "反无人机":
            self.debug_msg(f"当前选择项目: [{mode}]")
            if self.mainWin_thread_running == False:
                self.start_btn.clicked.connect(self.start_mainWin_thread())
                self.mainWin_thread_running = True

        elif mode == "并联机器人":
            self.debug_msg(f"当前选择项目: [{mode}]")
        else:
            self.debug_msg(f"请选择系统运行项目...")

    # 进度条加载线程控制器
    def setup_bar_thread(self):
        """创建进度条线程"""
        self.bar_thread = LoaderThread()
        # 设置进度条值
        self.bar_thread.valueChange.connect(self.progress_bar.setValue)
        self.bar_thread.loadComplete.connect(self.load_isComplete)

    @Slot()
    def start_bar_thread(self):
        """开启进度条加载线程"""
        if self.bar_thread_running == False:
            self.debug_msg("===============> 进度条线程启动！！！")
            self.setup_bar_thread()
            self.bar_thread.start()
            self.bar_thread_running = True
        else:
            self.debug_msg("===============> 进度条线程已经启动！！！")

    @Slot()
    def stop_bar_thread(self):
        """终止进度条线程"""
        if self.bar_thread_running == True:
            self.bar_thread.terminate()
            self.debug_msg("================> 进度条线程关闭！！！")
            self.bar_thread_running = False

    @Slot(bool)
    def load_isComplete(self, is_complete):
        """转接一个进度条是否加载完成的标志"""
        return is_complete

    # mainWindow控制器
    def setup_mainWin_thread(self):
        self.mainWin_thread = mainWinThread()
        self.mainWin_thread.setIdentity("mainWindow")
        self.mainWin_thread.sinOut.connect(self.debug_msg)

    def start_mainWin_thread(self):
        """启动线程"""
        if self.mainWin_thread_running == False:
            self.setup_mainWin_thread()
            self.mainWin_thread.myStart()
            self.mainWin_thread_running = True
        else:
            self.debug_msg("===============> mainWindow线程已经启动!!!")

    def stop_mainWin_thread(self):
        """停止mainthread线程"""
        if self.mainWin_thread_running == True:  # 标志位
            self.mainWin_thread.myStop()  # 线程终止
            self.mainWin_thread_running = False
        else:
            self.debug_msg("===============> mainWindow线程未开启!!!")

    def send_mainWin_show(self):
        """向mainWin发送是否显示自己
        @description:控制主窗口显示还是关闭,
        @param (bool)is_show
        """
        self.signal_show.emit(self.load_isComplete)

    @Slot()
    def stop_all_thread(self):
        """在这里将所有线程暂停/停止"""
        self.stop_bar_thread()
        self.stop_mainWin_thread()

    # 关闭所有线程
    @Slot()
    def exitProgram(self):
        if self.bar_thread_running == True:
            """在这里释放所有线程"""
            self.debug_msg("================> 所有线程已关闭!!!")
            self.bar_thread.quit()
            self.mainWin_thread.quit()


            sys.exit()
        else:
            sys.exit()


def test():
    app = QApplication()
    apply_stylesheet(app, theme="dark_blue.xml")
    load = LoadWin()
    load.show()
    app.exec()


# test()
