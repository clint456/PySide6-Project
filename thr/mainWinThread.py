import socket
import time
import sys


from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from win.mainWin import MainWin

from thr.MyThread import MyThread

class mainWinThread(MyThread):
    """启动mainWindow的入口线程"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.signal_show = False

    def run(self):
        self.print_msg("======================")
        
        self.main = MainWin()
        self.main.show()
        self.main.exec()
