from socket import socket
import time
import numpy as np
import cv2

from PySide6.QtCore import Signal 
from PySide6.QtGui import QPixmap,QImage
from thr.MyThread import MyThread


def matToQPixmap(frame):
    """ 将图像转换为 `QPixmap`
    @param
    ----------
    frame : cv2.typing.MatLike 格式
    """
    height, width = frame.shape[:2]
    if frame.ndim == 3:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    elif frame.ndim == 2:
        rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    temp_image = QImage(rgb.flatten(), width, height, QImage.Format_RGB888)
    temp_pixmap = QPixmap.fromImage(temp_image)
    return temp_pixmap
    
        
class ReceiveFrame(MyThread):
    """socket图像通信线程"""
    SignalFrame = Signal(QPixmap) # 用于传输图像的信号
    
    def __init__(self, parent=None, port=5555, address="localhost"):
        super().__init__(parent=parent)
        self.addr = (address,port)
        self.isStopped = False  # 控制线程开启和关闭
        self.__setupSocket()
        
    def __setupSocket(self):
        self.server =  socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建UDP套接字
        self.server.bind(self.addr) # 绑定端口
        self.server.setblocking(False) # 非阻塞模式
        self.print_msg(f"address is {self.addr}")
        
        
    def run(self):
        
        with self.server as s:  
            while not self.isStopped:
                data = None
                try:
                    data,_ = s.recvfrom(921600) # 非阻塞模式接受数据
                    receive_data = np.frombuffer(data,dtype='uint8')
                    r_img = cv2.imdecode(receive_data,1)
                    cv2.putText(r_img, "server", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    cv2.imshow("receive_serveer",r_img)  
                except OSError as e:
                    self.print_msg("Oops! 图像接受出现错误!")
                    pass
  
                self.SignalFrame.emit(matToQPixmap(r_img)) # 释放图像信号 
                
    def stop(self):
        '''停止从socket读取图像'''
        self.isStopped = True
        self.server.close()
    
    def loadImage(self):
        '''开始从socket读取图像'''
        self.isStopped = False
        self.start()