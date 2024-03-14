import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget

# 导入ui文件
from ui.mainUi_ui import *
from ui.loading_ui import *

# 加载页面
class ProcessWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)
    
    def setup_ui():
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    processWindow = ProcessWindow()
    processWindow.show()
    app.exec()

