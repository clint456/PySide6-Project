# -*- coding: utf-8 -*-

import time

from PySide6.QtCore import (QRunnable, QThreadPool, Signal, Slot, QSize)
from PySide6.QtWidgets import (QApplication, QPushButton, QLabel, QVBoxLayout, QWidget)


class MyWorker(QRunnable):

    def __init__(self, func, signal, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signal = signal

    def run(self):
        res = self.func(*self.args, **self.kwargs)
        # 任务完成后发出信号
        self.signal.emit(res)


def do_something():
    time.sleep(1)
    return 'the function execution completed!'


class MainWindow(QWidget):
    signal = Signal(str)

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

    @Slot(str)
    def thread_finished(self, res):
        self.label.setText('This is a label => ' + res)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
