# -*- coding: utf-8 -*-
import logging
import time

from PySide6.QtCore import (QRunnable, QThreadPool, Signal, Slot, QSize)
from PySide6.QtWidgets import (QApplication, QPushButton, QLabel, QVBoxLayout, QWidget)


class LoadWindow(QRunnable):
    def __init__(self):
        super().__init__()


    def run(self):
        while(True):
            logging.info("hello LoadWindow")
            time.sleep(0.5)

    #TODO 设置任务线程是否自动销毁
    def setAutoDelete(self, autoDelete: bool) -> None:
        return super().setAutoDelete(autoDelete)