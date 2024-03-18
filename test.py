import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget
from PySide6.QtCore import QThread,Signal

# 导入ui文件
from ui.mainUi_ui import *
from ui.loading_ui import *


class MyThread(QThread):

    # 数据传输信号
    data_signal = Signal(int)
    # 错误传输信号
    error_signal = Signal(str)
    # 任务结束信号
    finish_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def pause_thread(self):
        # 在新线程中执行的暂停的代码
        pass

    def resume_thread(self):
        # 在新线程中执行的恢复的代码
        pass

    def run(self):
		# 在新线程中执行的代码
        while True:
            print("子线程正在运行...")
            time.sleep(1)
        

# 加载页面
class ProcessWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置ui
        self.setup_ui()
        # 启动线程
        self.setup_thread()

        self.start_thread()

    
    def setup_ui(self):
		# GUI界面绘制
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)
        pass

    def setup_thread(self):
        self.thread = MyThread()

    def start_thread(self):
        self.thread.start()

    def paused_thread(self):
        self.thread.pause_thread()

    def resume_thread(self):
        self.thread.resume_thread()
        
    def stop_thread(self):
        self.thread.quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    processWindow = ProcessWindow()
    processWindow.show()
    app.exec()

