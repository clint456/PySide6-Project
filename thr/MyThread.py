import time
from datetime import datetime
from PySide6.QtCore import QThread,Signal

class MyThread(QThread):
    '''
    子线程接口类：
        调用步骤： 
            1.创建线程对象 <thread_name> = MyThread()
            2.设置线程名称 <thread_name>.setIdentity(str(thread_name))
            3.设置回调函数 接收子线程数据 
    说明：如果需要添加功能，建议继承该模块，添加具体功能
    '''
    sinOut = Signal(str)

    def __init__(self,parent=None):
        super(MyThread,self).__init__(parent)
        self.identity = None

    def setIdentity(self,text):
        self.identity = text
        
    def print_msg(self,str):
        self.sinOut.emit(f'[{self.identity}] info : {str}')
    
    def run(self): 
        while True:  
            # 发射信号
            self.print_msg(datetime.now())
            
            time.sleep(0.1)
    
    
    def myStart(self) -> None:
        self.sinOut.emit(f'================> {self.identity} is start !!!')
        self.start()
    
    def myStop(self) -> None:
       
        self.terminate()
        self.sinOut.emit(f'================>  {self.identity} is stop !!!')

        
     