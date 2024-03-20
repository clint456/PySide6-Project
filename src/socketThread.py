import socket
import time

from MyThread import MyThread

class socketThread(MyThread):
    '''socket通信线程'''
    def __init__(self,port=12345,address='localhost'):
        super().__init__()
        self.port = port
        self.address = address
        
    def run(self):
        while True:
            self.print_msg(f'port is {self.port}, address is {self.address}')
            time.sleep(1)
            pass
    