import sys
import time

from PySide6.QtCore import (QMutex, QMutexLocker, QThread, QWaitCondition,
                            Signal, Slot)
from PySide6.QtGui import Qt,QGuiApplication
from PySide6.QtWidgets import (QApplication, QProgressBar, QPushButton,
                               QVBoxLayout, QWidget)
from PySide6 import QtWidgets
from qt_material import apply_stylesheet

from ui.loading_ui import Ui_LoadingScreen
from win.antiDroneWin import AntiDrone

class LoadWin(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)  # 初始化父类
        self.currentProject = None
        self.current_project_index = 0  # 用于切换项目

        self.bar_thread_running = False  # 标记线程是否正在运行
        self.__redefine_window_border()
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
        self.center()

    def __load_connect(self):
        """初始化连接信号与槽"""
        self.start_btn.clicked.connect(self.startCurrentProject)
        self.stop_btn.clicked.connect(self.stopAllThread)
        self.exit_btn.clicked.connect(self.exitProgram)
        self.select_program.activated.connect(self.changeProgram)
    
    def center(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height() - size.height()/2)) # 窗口居中
        
    def debug_msg(self, str):
        """打印信息输出到Gui面板"""
        self.debug_bw.append(str)  # 添加到面板输出流
        print(str)
    
    def start_antiDrone(self):
        self.currentProject = AntiDrone()
        

    @Slot(bool)
    def load_isComplete(self, is_complete):
        """转接一个进度条是否加载完成的标志"""
        if(is_complete):
            self.debug_msg(f'\n加载完成!!!')
            self.currentProject.show()
        else:
            self.debug_msg(f'======= 正在加载中 =======>')

                
    def startCurrentProject(self):
        '''启动项目'''
        if(self.bar_thread_running):
             self.debug_msg("===============> 不得重复加载！！！")
        else:
            if self.current_project_index == 0: 
                self.debug_msg(f'请选择当前要启动的项目！！！')
            elif self.current_project_index == 1:
                self.start_bar_thread()
                self.debug_msg(f'反无人机项目启动')     
                self.start_antiDrone()
            elif self.current_project_index == 2:
                #TODO 并联机器人项目
                self.debug_msg(f'并联机器人项目待开发...')
            else:
                self.debug_msg(f'项目启动，出现未知错误') 
    
    
    # 项目切换控制器
    @Slot(int)
    def changeProgram(self, index):
        """判断当前选择要启动的项目"""
        mode = self.select_program.itemText(index)
        """判断当前系统运行模式"""
        if mode == "反无人机":
            self.debug_msg(f"当前选择项目: [{mode}]")
            self.current_project_index = 1
        elif mode == "并联机器人":
            self.debug_msg(f"当前选择项目: [{mode}]")
            self.current_project_index = 2
        else:
            self.debug_msg(f"请选择系统运行项目...")
            self.current_project_index = 0

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
            self.debug_msg("===============> 开始加载！！！")
            self.setup_bar_thread()
            self.bar_thread.start()
            self.bar_thread_running = True
        else:
            self.debug_msg("===============> 不得重复加载！！！")
    @Slot()
    def stop_bar_thread(self):
        """终止进度条线程"""
        if self.bar_thread_running == True:
            self.bar_thread.terminate()
            self.debug_msg("================> 停止加载！！！")
            self.bar_thread_running = False

    @Slot()
    def stopAllThread(self):
        """在这里将所有线程暂停/停止"""
        if(self.bar_thread_running):
            self.stop_bar_thread()
            self.currentProject.close()
   
    # 关闭所有线程
    @Slot()
    def exitProgram(self):
        if self.bar_thread_running == True:
            """在这里释放所有线程"""
            self.bar_thread.quit()
            self.currentProject.close()
            self.close()
            sys.exit()
        else:
            sys.exit()

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
                    return  # 当进度条增加为100时，返回并退出线程
                else:
                    self.set_loadComplete(False)
                    self.progress_value += 1
                    self.valueChange.emit(self.progress_value)  # 发送进度条值变化
                    time.sleep(0.01)



def test():
    app = QApplication()
    apply_stylesheet(app, theme="dark_blue.xml")
    load = LoadWin()
    load.show()
    app.exec()


