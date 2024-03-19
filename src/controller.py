
import logging
import sys
import time
import keyboard

from PySide6.QtCore import (Signal,Slot)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


sys.path.append("..")
from module import (ThreadPool,MyWorker,SocketModule,
                    LoadWindow,MainWindow,MySignals,NewWindow)


def worker_1():
    time.sleep(1)
    return f'线程1 的操作'

def worker_2():
    time.sleep(1)
    return f'线程2 的操作'


signal_worker1 = MySignals.MySignals()
signal_worker2 = MySignals.MySignals()

# 创建工作类
work_list = []

myWork1 = MyWorker.MyWorker(signal_worker1.text_print,worker_1)
myWork2 = MyWorker.MyWorker(signal_worker2.text_print,worker_2)
work_list.append(myWork1)
work_list.append(myWork2)
# 创建线程池,设置一次最多运行10个线程
myPool = ThreadPool.MyPool(10,work_list)

class Controller(QWidget):
    
    
    def __init__(self):
        super().__init__()
        # 设置打印日志的级别，level级别以上的日志会打印出
        logging.basicConfig(level=logging.DEBUG)
        self.window1 = NewWindow.AnotherWindow()
        self.window2 = NewWindow.AnotherWindow()
        signal_worker1.text_print.connect(self.signal_worker1_trig)
        signal_worker2.text_print.connect(self.signal_worker2_trig)
        myPool.initPool()
        # 启动线程池
        myPool.tryPool()
        
        self.setup_ui()

       
    def setup_ui(self):

        self.setWindowTitle('控制器')
        # 布局管理器
        layout = QVBoxLayout()

        button1 = QPushButton("open Main")
        button1.clicked.connect(self.toggle_window1)
        layout.addWidget(button1)

        button2 = QPushButton("open load")
        button2.clicked.connect(self.toggle_window2)
        layout.addWidget(button2)

        self.setLayout(layout)

    def toggle_window1(self):
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()

    def toggle_window2(self):
        if self.window2.isVisible():
            self.window2.hide()
        else:
            self.window2.show()

    @Slot(str)
    def signal_worker1_trig(res):
            logging.info(f"signal_worker1_res: {res}")

    @Slot(str)
    def signal_worker2_trig(res):
            logging.info(f"signal_worker2_res: {res}")


app = QApplication(sys.argv)
controller = Controller()
controller.show()
app.exec()
