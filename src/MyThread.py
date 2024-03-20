import time
from datetime import datetime
from PySide6.QtCore import QThread,Signal

class MyThread(QThread):
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

        
     