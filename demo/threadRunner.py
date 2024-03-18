# -*- coding: utf-8 -*-

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
        

    def SpinTask():
        print(f"Worker started")
        time.sleep(1)  # 模拟一些耗时的工作
        print(f"Worker finished")

    def run(self):
        while True:
            res = self.func(*self.args, **self.kwargs)
            print(f"程序运行的结果是: {res}")
        # #TODO 执行循环任务
        # self.SpinTask()

        # # 任务完成后发出信号    
        # self.signal.emit(res)

    

        
    #TODO 线程销毁
    def setAutoDelete(self, autoDelete: bool) -> None:
        return super().setAutoDelete(autoDelete)
        
