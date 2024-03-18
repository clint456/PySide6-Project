import sys
import time
from PySide6.QtCore import (QRunnable, QThreadPool, Qt,Signal)
from threadRunner import MyWorker

'''线程池'''
class MyPool(QThreadPool):
    class_variable = "this is a class variable"

    def __init__(self,Max_thread,signal,Work):
        super().__init__()
        # 最大线程数
        self.Max_thread = Max_thread
        # 工作任务
        self.Work = Work
        # 信号
        self.signal = signal

    # 初始化线程
    def initPool(self):
        # 创建线程池
        self.MyThreadPool = QThreadPool()
        # 设置最大线程数
        self.MyThreadPool.setMaxThreadCount(self.Max_thread)
    
    # 线程启动
    def startPool(self):
        if self.Work is not None:
            # 将任务添加到线程池
            try:
                self.MyThreadPool.start(self.Work)
            except Exception as e:
                print(f'threadPool 启动失败: {e}')
                sys.exit("some error message")
                sys.exit(0)
        else:
            print("错误，没有任务需要进行执行！")
            sys.exit("some error message")
    
    def wait_for_done(self):
    # 在等待所有任务完成之前，阻塞主线程
        self.MyThreadPool.waitForDone()
        print("All tasks completed")
    
    @classmethod
    def show_class_variable(cls):
        print(cls.class_variable)

def doSomething():

    time.sleep(1)
    return f'耗时操作'
    

def main():
    signal = Signal(int)
    myWork = MyWorker(signal,doSomething)
    
    # 类级别的方法
    MyPool.show_class_variable()

    myPool = MyPool(2,signal,myWork)

    # 实例方法
    myPool.initPool()
    myPool.startPool()
    myPool.wait_for_done()

if __name__ == "__main__":
    main()

