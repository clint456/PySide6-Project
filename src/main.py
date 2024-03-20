# -*- coding: utf-8 -*-
"""
    多线程信号槽通信
"""

import sys
import logging
from datetime import datetime
from PySide6.QtWidgets import  QApplication,QWidget,QMainWindow
from PySide6.QtCore import Signal,QObject,QTimer,QEventLoop
from PySide6.QtGui import QTextCursor
from qt_material import apply_stylesheet

from MyThread import MyThread

sys.path.append("..")
from ui import mainUi_ui


class Signal_terminal(QObject):
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
        sys.stdout = Signal_terminal()
        sys.stdout.text_update.connect(self.updateText)
        
        # 创建一个线程实例并设置名称、变量、信号槽
        self.thread1 = MyThread()
        self.thread1.setIdentity("thread1")
        self.thread1.sinOut.connect(self.outText)
        
        self.setup_btn()
        
        
        
    def setup_ui(self):
        '''加载ui文件 初始化'''
        self.main_ui = mainUi_ui.Ui_MainWindow()
        self.main_ui.setupUi(self)
    
    def setup_btn(self):
        '''按键设置'''
        self.main_ui.start_btn.clicked.connect(self.startClick)
        self.main_ui.stop_btn.clicked.connect(self.stopClick)
        
    def outText(self,text):
        '''更新子线程输出'''
        print(text)
        logging.info(text)
        
    def updateText(self,text):
        '''更新控制台输出'''
        cursor = self.main_ui.debug_msg.textCursor()
        self.main_ui.debug_msg.setFontPointSize(7)
        self.main_ui.debug_msg.setTextColor('white')
        self.main_ui.debug_msg.insertPlainText(text)
        self.main_ui.debug_msg.setTextCursor(cursor)
        self.main_ui.debug_msg.ensureCursorVisible()

    
    def stopClick(self):
        self.thread1.myStop()
        
    def startClick(self):
        """Runs the main function."""
        self.thread1.myStart()
        
       
    
   
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme='dark_blue.xml')
    main = Main()
    main.show()
    app.exec()
