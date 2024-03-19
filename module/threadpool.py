import sys
import logging
import time
from PySide6.QtCore import (QRunnable, QThreadPool, Qt,Signal)


'''线程池'''
class MyPool(QThreadPool):
    def __init__(self,Max_thread,Work):
        super().__init__()
        # 最大线程数
        self.Max_thread = Max_thread
        # 工作任务
        self.Work = Work


    # 初始化线程
    def initPool(self):
        # 创建线程池
        self.MyThreadPool = QThreadPool()
        # 设置最大线程数
        self.MyThreadPool.setMaxThreadCount(self.Max_thread)
    
    def tryPool(self):
        '''线程启动
            Work是一个Worker任务列表
        '''
        if self.Work:
            # 将任务添加到线程池
            for item in self.Work:
                if (self.MyThreadPool.tryStart(item) == False):
                    logging.error("任务启动失败")
                    sys.exit(0)
            logging.info("所有线程启动完毕！")
        else:
            logging.error("错误，没有任务需要进行执行！")
            sys.exit(0)

    def tryWork(self):
        '''线程启动
            Work是一个单独Worker任务
        '''
        if self.Work:
            if (self.MyThreadPool.tryStart(self.Work) == False):
                    logging.error("任务启动失败")
                    sys.exit(0)
            logging.info("线程启动完毕！")
        else:
            logging.error("错误，没有Worker需要进行执行！")
            sys.exit(0)
    
    def stopPool(self):
    # 在等待所有任务完成之前，阻塞主线程
        logging.warning("触发线程退出！")
        self.MyThreadPool.waitForDone(self,1)
        

    




