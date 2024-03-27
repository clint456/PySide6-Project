# -*- coding: utf-8 -*-
"""
    多线程信号槽通信
"""

import sys
import logging
from datetime import datetime
from PySide6.QtWidgets import  QApplication,QWidget,QMainWindow,QMessageBox
from PySide6.QtCore import Signal,QObject,QTimer,QEventLoop,Slot

from thr.MyThread import MyThread 
from thr.socketThread import socketThread

from ui.mainUi_ui import Ui_MainWindow


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

class MainWin(QWidget):
    # 设置
    logging.basicConfig(level=logging.DEBUG)
  
    def __init__(self, parent = None):
        super(MainWin,self).__init__(parent)
        self.setup_ui()
        
        # 实时显示输出，将控制台输出重定向到界面中
        sys.stdout = Signal_Gui()
        sys.stdout.text_update.connect(self.updateText)
        
        
        # 创建一个线程实例并设置名称、变量、信号槽
        self.thread1 = MyThread()
        self.thread1.setIdentity("thread1")
        self.thread1.sinOut.connect(self.outText)
        
        #创建一个socket线程
        self.socket_thread =socketThread(port=8888,address="127.0.0.1")
        self.socket_thread.setIdentity("socket_thread")
        self.socket_thread.sinOut.connect(self.socketHandle)
     
        self.setup_btn()
        
        
    def setup_ui(self):
        '''加载ui文件 初始化'''
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        
    
    def setup_btn(self):
        '''按键设置'''
        self.main_ui.start_btn.clicked.connect(self.startDebugClick)
        self.main_ui.stop_btn.clicked.connect(self.stopDebugClick)
        self.main_ui.frame_sw.activated.connect(self.handleCombobox)
        self.main_ui.mode_sw.activated.connect(self.handleModeChange)
        
    @Slot(str)  
    def outText(self,text):
        '''更新demo子线程输出'''
        print(text)
    
    @Slot(str)  
    def updateText(self,text):
        '''更新控制台输出'''
        cursor = self.main_ui.debug_msg.textCursor()
        self.main_ui.debug_msg.setFontPointSize(11)
        self.main_ui.debug_msg.setTextColor('white')
        self.main_ui.debug_msg.append(f'{text}')
        self.main_ui.debug_msg.setTextCursor(cursor)
        self.main_ui.debug_msg.ensureCursorVisible()
     
    def stopDebugClick(self):
        '''定义debug窗口按键控制操作'''
        self.thread1.myStop()
        
    def startDebugClick(self):
        self.thread1.myStart()
    
    @Slot(str)
    def socketHandle(self,text):
        '''socket回调函数处理'''
        print(text)
        logging.info(text)
    
    #TODO 视频源切换器
    @Slot(int)    
    def handleCombobox(self,index):
        # 获取控件当前的模式
        mode = self.main_ui.frame_sw.itemText(index) 
        '''判断当前该使用什么视频源输入'''
        if(mode != "视频输入"):
            if(mode == 'socket'):
                print(f"当前视频源: {mode}")
                self.socket_thread.myStart()          
            else:
                self.socket_thread.myStop()   
                          
            if(mode == 'video'):
                #TODO 读取视频路径
                print(f"当前视频源: {mode}")
                
                pass
            
            if(mode == 'local'):
                #TODO 打开usb摄像机
                print(f"当前视频源: {mode}")
                pass
            
            
        else: 
            print("请设置视频输入模式....")
   
    
    #TODO 模式切换器
    @Slot(int)
    def handleModeChange(self,index):
        mode = self.main_ui.mode_sw.itemText(index) 
        '''判断当前系统运行模式'''
        if(mode == '巡航模式' ): 
            print(f"当前模式: {mode}" )   
                
            pass
        elif(mode == '跟踪模式'):
            print(f"当前模式: {mode}" )
            
            pass
        elif(mode == '开火模式'):
            print(f"当前模式: {mode}" )
            
            pass
        else:
            print("请选择系统运行模式...")
        
    def closeEvent(self, event):
        '''
        @description: 退出窗口
        @param: MainWindow 窗口标题
                Are you sure to quit? 窗口显示内容
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No窗口按钮部件
                QtGui.QMessageBox.No默认焦点停留在NO上
        '''
      
        reply = QMessageBox.question(self, 'MainWindow',
                                        "Are you sure to quit?",
                                        QMessageBox.Yes |
                                        QMessageBox.No,
                                        QMessageBox.No)
        # 判断返回结果处理相应事项
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
            
    