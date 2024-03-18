
import logging
import sys
import time

from PySide6.QtCore import Signal
import keyboard

sys.path.append("..")
from module import ThreadPool,MyWorker,SocketModule,LoadWindow,MainWindow

def worker_1():

    time.sleep(1)
    return f'线程1 的操作'

def worker_2():

    time.sleep(1)
    return f'线程2 的操作'

def main_window():
    return f"main window 的操作"

def main():
    # 设置打印日志的级别，level级别以上的日志会打印出
    # level=logging.DEBUG 、INFO 、WARNING、ERROR、CRITICAL

    # 此处进行Logging.basicConfig() 设置，后面设置无效
    logging.basicConfig(level=logging.DEBUG)

    signal_worker1 = Signal(int)
    signal_worker2 = Signal(int)
    signal_socket = Signal(int)
    signal_main = Signal(int)
    signal_load = Signal(int)


    # 创建工作类
    work_list = []
    signal_list = {'work1':signal_worker1,'work2':signal_worker2,'socket':signal_socket,'main':signal_main,'load':signal_load}

    myWork1 = MyWorker.MyWorker(signal_worker1,worker_1)
    myWork2 = MyWorker.MyWorker(signal_worker2,worker_2)

    socketWorker = SocketModule.SocketModule()
    mainWindow = MainWindow.MainWindow()
    loadWindow = LoadWindow.LoadWindow()

    
    work_list.append(myWork1)
    work_list.append(myWork2)
    work_list.append(socketWorker)
    work_list.append(mainWindow)
    work_list.append(loadWindow)

    # 创建线程池,设置一次最多运行10个线程
    myPool = ThreadPool.MyPool(10,signal_list,work_list)

    # 实例方法
    myPool.initPool()
    myPool.tryPool()

    # 等待触发结束
    while(True):
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            logging.error('Ctrl+C被按下')
            myPool.stopPool()
            break


if __name__ == "__main__":
    main()
