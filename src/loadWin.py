import sys
import time 
import sys
from PySide6.QtCore import (QThread, QWaitCondition, QMutex, Signal, QMutexLocker,Slot)
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QProgressBar, QApplication)
from PySide6.QtGui import Qt

from qt_material import apply_stylesheet

from ui.loading_ui import Ui_LoadingScreen

class LoaderThread(QThread):
    '''进度条加载线程'''
    valueChange  = Signal(int) #自定义信号，用于发送进度值的变化
    
    def __init__(self,parent = None):
        super().__init__(parent=parent)
        self.progress_value = int(0)          # 设置进度条初始值
        self.is_paused = bool(0)           # 标记线程是否暂停
        self.mutex = QMutex()            # 互斥锁，用于线程同步
        self.cond = QWaitCondition()    # 设置等待条件，用于暂停和恢复
    
    def pause_thread(self):
        '''设置线程为暂停状态'''
        with QMutexLocker(self.mutex):
            self.is_paused = True 
            
    def resume_thread(self):
        '''设置线程为非暂停状态'''
        if self.is_paused:
            with QMutexLocker(self.mutex):  
                '''锁定互斥锁的对象'''
                self.is_paused = False # 设置线程为非暂停状态
                self.cond.wakeOne() # 唤醒一个等待的线程
                
        
    def run(self):
        while True:
            with QMutexLocker(self.mutex):
                while self.is_paused:
                    self.cond.wait(self.mutex) # 当线程为暂停状态时，进入等待
                
                if self.progress_value >= 100:
                    self.progress_value = 0
                    print("================> 进度加载完成")
                    return # 当进度条增加为100时，返回并退出线程
                self.progress_value += 1
                self.valueChange.emit(self.progress_value) # 发送进度条值变化
                time.sleep(0.1)

class LoadWin(QWidget):
    #TODO 这此添加判断主页面是否加载完成的信号
    
    def __init__(self,parent=None):
        super().__init__(parent=parent) # 初始化父类
        
        self.thread_running = False # 标记线程是否正在运行
        self.__redefine_window_border()
        self.__setup_ui()
        self.load_connect()
    
    def __redefine_window_border(self):
        '''
        设置无边框
        '''
        self.setWindowFlag(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint
                    | Qt.WindowMinimizeButtonHint| Qt.WindowMaximizeButtonHint)
    
    def __setup_ui(self):
        '''初始化designer组件'''
        self.load_ui = Ui_LoadingScreen()
        self.load_ui.setupUi(self) # 初始化designer界面
        # 获取designer界面组件对象
        self.progress_bar = self.load_ui.loadProgressBar
        self.start_btn = self.load_ui.startButton
        self.stop_btn = self.load_ui.stopButton
        self.exit_btn = self.load_ui.exitButton
        self.debug_bw = self.load_ui.debugBrowser
        self.debug_bw.setFontPointSize(8)
        self.debug_bw.setTextColor('white')
        
        
    def load_connect(self):
        '''初始化连接信号与槽'''
        self.start_btn.clicked.connect(self.start_thread)
        self.stop_btn.clicked.connect(self.stop_thread)
        self.exit_btn.clicked.connect(self.exitProgram)
        
    def setup_thread(self):
        '''创建进度条线程'''
        self.thread = LoaderThread()
        # 设置进度条值
        self.thread.valueChange.connect(self.progress_bar.setValue)
        
        
    @Slot()
    def start_thread(self):
        if self.thread_running == False:
            self.debug_msg("===============> 进度条线程启动！！！")
            self.setup_thread()
            self.thread.start()
            self.thread_running = True
        else:
            self.debug_msg("===============> 进度条线程已经启动！！！")
        
        
    
    @Slot()
    def stop_thread(self):
        # 结束
        if self.thread_running == True:
            self.thread.terminate()
            self.debug_msg("================> 进度条线程关闭！！！")
            self.thread_running = False
        else:
            self.debug_msg("===============> 进度条线程已经关闭！！！")
            
    @Slot()
    def exitProgram(self):
       if self.thread_running == True:
            self.thread.quit()
            self.debug_msg("================> 进度条线程已关闭！！！")
            sys.exit()
       else:
            sys.exit()
            
    def debug_msg(self,str):
        self.debug_bw.append(str)
        
        
def test():
    app = QApplication()
    apply_stylesheet(app,theme='dark_blue.xml')
    load = LoadWin() 
    load.show()
    app.exec()
        
#test()