import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget
from PySide6.QtCore import QThread
# 导入ui文件
from ui.mainUi_ui import *
from ui.loading_ui import *


class MyThread(QThread):

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
        pass
        

# 加载页面
class ProcessWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)


        # 启动线程
        self.setup_thread()

    
    def setup_ui(self):
		# GUI界面绘制
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

