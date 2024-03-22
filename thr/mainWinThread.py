import socket
import time
from PySide6.QtCore import Signal

from thr.MyThread import MyThread

class mainWinThread(MyThread):
    '''启动mainWindow的入口线程'''

    
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.signal_show = False 
        self.print_msg("mainWindow线程启动")
    def run(self):
        
        while True:
            
            
            time.sleep(1)
            pass
        
    