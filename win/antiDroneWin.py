# -*- coding: utf-8 -*-
"""
    多线程信号槽通信
"""

import sys
import cv2
import logging
from datetime import datetime
from PySide6.QtWidgets import  (
    QApplication,
    QWidget,
    QMainWindow
    ,QMessageBox
)
from PySide6.QtCore import (
    Signal,
    QObject,
    QTimer,
    QEventLoop,
    Slot,
    Qt
)
from PySide6.QtGui import QPixmap
from thr.MyThread import MyThread 
from thr.receiveFrameThread import  ReceiveFrame

from ui.mainUi_ui import Ui_MainWindow


class Signal_Gui(QObject):
    '''重定向终端到Text Widget'''
    text_update = Signal(str)
    
    def write(self,text):
        self.text_update.emit(str(text))
        
    def flush(self):
        pass
        
# 备份系统重定向
stdout_temp = sys.stdout   
def resetToTerminal():
    '''还原重定向'''
    sys.stdout = stdout_temp    

class AntiDrone(QWidget):
    # 设置日志输出模式 
    # logging 输出到终端， print 输出到GUI终端页面
    logging.basicConfig(level=logging.DEBUG)
  
    def __init__(self, parent = None):
        super(AntiDrone,self).__init__(parent)
        self.currentSource = 0 
        self.__setup_ui()  
        self.__setup_out_to_widget()
        self.setup_FrameReceiveSocket(port=5555,address="127.0.0.1") # 视频接收线程初始化
        self.setup_btn()
        
    def setup_FrameReceiveSocket(self,port,address):
        '''创建图像接受线程'''
        self.frameReceiveThread =ReceiveFrame(port=port,address=address)
        self.frameReceiveThread.setIdentity("socket_thread")
        self.frameReceiveThread.sinOut.connect(self.frameReceiveHandle)
        self.frameReceiveThread.SignalFrame.connect(self.socket_updateFrame)
        
    def socket_updateFrame(self,Frame):
        '''socket更新视频流'''
        map = Frame.scaled(self.main_ui.frame_label.size(), aspectMode = Qt.KeepAspectRatioByExpanding) # 设置画面平铺
        if(self.currentSource == 1):
            self.main_ui.frame_label.setPixmap(map)

    def __setup_out_to_widget(self):
        '''实时显示输出，将控制台输出重定向到界面中'''
        sys.stdout = Signal_Gui()
        sys.stdout.text_update.connect(self.updateText)
        
    def __setup_ui(self):
        '''加载ui文件 初始化'''
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

    
    
    def setup_btn(self):
        '''信号连接'''
        self.main_ui.start_btn.clicked.connect(self.startDebugClick)
        self.main_ui.stop_btn.clicked.connect(self.stopDebugClick)
        self.main_ui.frame_sw.activated.connect(self.handleCombobox)
        self.main_ui.mode_sw.activated.connect(self.handleModeChange)
        
    @Slot(str)  
    def outText(self,text):
        '''更新demo子线程输出
            (此时stdout已经绑定到了GUI终端上'''
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
        pass
        
    def startDebugClick(self):
        pass
    
    @Slot(str)
    def frameReceiveHandle(self,text):
        '''socket回调函数处理'''
        print(text)
        logging.info(text)
    
    #TODO 视频源切换器
    @Slot(int)    
    def handleCombobox(self,index):
        # 获取控件当前的模式
        mode = self.main_ui.frame_sw.itemText(index) 
        '''判断当前该使用什么视频源输入'''
        if(mode == 'socket'):
            print(f"当前视频源: {mode}")
            self.currentSource = 1
            self.frameReceiveThread.myStart()          
                   
        elif(mode == 'video'):
            #TODO 读取视频路径
            self.currentSource = 2
            print(f"当前视频源: {mode}")      
            self.frameReceiveThread.myStop()    
            pass
        
        elif(mode == 'local'):
            #TODO 打开usb摄像机
            self.currentSource = 3
            print(f"当前视频源: {mode}")
            self.frameReceiveThread.myStop()  
            cap = cv2.VideoCapture(0)
            # 设置镜头分辨率，默认是640x480 
            self.local_frame.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
            self.local_frame.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)     
        else:
            print("请选择当前视频源....")
            self.frameReceiveThread.myStop()  
               
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
            
            
    