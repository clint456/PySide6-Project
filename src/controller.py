
import logging
import sys
import time

from PySide6.QtCore import Signal
import keyboard

sys.path.append("..")
from module.threadpool import MyPool
from module.threadRunner import MyWorker


def worker_1():

    time.sleep(1)
    return f'线程1 的操作'

def worker_2():

    time.sleep(1)
    return f'线程2 的操作'

def main():
    # 设置打印日志的级别，level级别以上的日志会打印出
    # level=logging.DEBUG 、INFO 、WARNING、ERROR、CRITICAL

    # 此处进行Logging.basicConfig() 设置，后面设置无效
    logging.basicConfig(level=logging.DEBUG)

    signal = Signal(int)
    # 创建工作类
    work_list = []
    myWork1 = MyWorker(signal,worker_1)
    myWork2 = MyWorker(signal,worker_2)
    
    work_list.append(myWork1)
    work_list.append(myWork2)

    # 创建线程池
    myPool = MyPool(2,signal,work_list)

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
