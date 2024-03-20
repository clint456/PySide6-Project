# -*- coding: utf-8 -*-
"""
    多线程信号槽通信
"""

import sys
import logging
from datetime import datetime
from PySide6.QtWidgets import  QApplication,QWidget,QMainWindow
from PySide6.QtCore import Signal,QObject,QTimer,QEventLoop,Slot
from PySide6.QtGui import QTextCursor
from qt_material import apply_stylesheet

from MyThread import MyThread
from socketThread import socketThread

sys.path.append("..")
from ui import mainUi_ui


class Signal_Gui(QObject):
    '''控制台信号'''
    text_update = Signal(str)
    
    def write(self,text):
        self.text_update.emit(str(text))
        '''ProcessEventsFlag'''
        loop = QEventLoop()
        # 调节刷新速度
        QTimer.singleShot(10, loop.quit)
        loop.exec()
        QApplication.processEvents()
        
    def flush(self):
        pass
        
# 备份系统重定向
stdout_temp = sys.stdout   
def resetToTerminal():
    '''还原重定向'''
    sys.stdout = stdout_temp    

class Main(QMainWindow):
    # 设置
    logging.basicConfig(level=logging.DEBUG)
  
    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        self.setup_ui()
        
        # 实时显示输出，将控制台输出重定向到界面中
        sys.stdout = Signal_Gui()
        sys.stdout.text_update.connect(self.updateText)
        # 创建一个线程实例并设置名称、变量、信号槽
        self.thread1 = MyThread()
        self.thread1.setIdentity("thread1")
        self.thread1.sinOut.connect(self.outText)
        
        #创建一个socket线程
        self.socket_thread = socketThread(port=8888,address="127.0.0.1")
        self.socket_thread.setIdentity("socket_thread")
        self.socket_thread.sinOut.connect(self.socketHandle)
     
        self.setup_btn()
        
        
    def setup_ui(self):
        '''加载ui文件 初始化'''
        self.main_ui = mainUi_ui.Ui_MainWindow()
        self.main_ui.setupUi(self)
        
    
    def setup_btn(self):
        '''按键设置'''
        self.main_ui.start_btn.clicked.connect(self.startDebugClick)
        self.main_ui.stop_btn.clicked.connect(self.stopDebugClick)
        self.main_ui.frame_sw.highlighted.connect(self.handleCombobox)
        
        
    def outText(self,text):
        '''更新demo子线程输出'''
        print(text)
        # logging.info(text)
        
    def updateText(self,text):
        '''更新控制台输出'''
        cursor = self.main_ui.debug_msg.textCursor()
        self.main_ui.debug_msg.setFontPointSize(7)
        self.main_ui.debug_msg.setTextColor('white')
        self.main_ui.debug_msg.insertPlainText(text)
        self.main_ui.debug_msg.setTextCursor(cursor)
        self.main_ui.debug_msg.ensureCursorVisible()
        
    def stopDebugClick(self):
        '''定义debug窗口按键控制操作'''
        self.thread1.myStop()
        
    @Slot (str) 
    def startDebugClick(self):
        self.thread1.myStart()
    
    @Slot(str)
    def socketHandle(self,text):
        '''socket回调函数处理'''
        print(text)
        logging.info(text)
    
    #TODO视频传输切换
    @Slot(int)    
    def handleCombobox(self,index):
        '''定义socket传输按键'''
        logging.info(f'该项对应的文本为： {self.main_ui.frame_sw.itemText(index)}')
        if(self.main_ui.frame_sw.itemText(index) == 'socket'):
            self.socket_thread.myStart()
        else:
            self.socket_thread.myStop()
            pass    
    
    #TODO 

        
       
    
   
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme='dark_blue.xml')
    main = Main()
    main.show()
    app.exec()
