# -*- coding: utf-8 -*-
import logging
import time

from PySide6.QtCore import (QRunnable, QThreadPool, Signal, Slot, QSize)
from PySide6.QtWidgets import (QApplication, QPushButton, QLabel, QVBoxLayout, QWidget)

'''工作任务类'''
class MyWorker(QRunnable):

    def __init__(self, signal,func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signal = signal
        
    def run(self):
        while True:
            #TODO 执行循环任务
            res = self.func(*self.args, **self.kwargs)
            logging.info(f"程序运行的结果是: {res}")
       
        # # 任务完成后发出信号    
        # self.signal.emit(res)

        
    #TODO 设置任务线程是否自动销毁
    def setAutoDelete(self, autoDelete: bool) -> None:
        return super().setAutoDelete(autoDelete)
        