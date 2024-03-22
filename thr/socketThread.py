import socket
import time

from .MyThread import MyThread

class socketThread(MyThread):
    '''socket通信线程'''
    def __init__(self,parent=None,port=12345,address='localhost'):
        super().__init__(parent=parent)
        self.port = port
        self.address = address
        
    def run(self):
        self.print_msg(f'port is {self.port}, address is {self.address}')
        while True:
            
            
            time.sleep(1)
            pass
    
    #TODO 视频流接收
    def socket_frame_handle(self):
        pass
    
    #TODO 向下位机交互数据
    def socket_data_handle(self):
        pass
    