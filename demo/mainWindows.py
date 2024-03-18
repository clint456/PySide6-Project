# -*- coding: utf-8 -*-

import time

from PySide6.QtCore import (QRunnable, QThreadPool, Signal, Slot, QSize)
from PySide6.QtWidgets import (QApplication, QPushButton, QLabel, QVBoxLayout, QWidget)

from demo.threadRunner import MyWorker



def do_something():
    # time.sleep(0.1)

    return 9999


class MainWindow(QWidget):
    signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.thread_pool = QThreadPool()
        self.setup_ui()
        self.button.clicked.connect(self.setup_thread)

    def setup_ui(self):
        self.setWindowTitle('demo')
        self.resize(QSize(250, 180))
        # 创建一个垂直布局
        layout = QVBoxLayout()
        # 创建一个标签
        self.label = QLabel('This is a label => ')
        layout.addWidget(self.label)
        # 创建一个按钮
        self.button = QPushButton('execute')
        layout.addWidget(self.button)
        # 将布局设置为主窗口的布局
        self.setLayout(layout)
        # 显示窗口
        self.show()

    def setup_thread(self):
        worker = MyWorker(do_something, self.signal)
        self.thread_pool.start(worker)
        self.signal.connect(self.thread_finished)

    @Slot(int)
    def thread_finished(self, res):
        self.label.setText('This is a label => ' + f'{res}')
        print(f'{res}')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()