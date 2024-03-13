from loader import Loader

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile,QTimer
from qt_material import apply_stylesheet

import sys

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.init_ui()

    def init_ui(self):
        # 创建主窗口内容
        self.setWindowTitle('Main Application')
        self.setGeometry(300, 300, 400, 200)

        # 在这里可以添加主窗口的其他组件和功能

if __name__ == "__main__":
    # 创建应用程序
    app = QApplication(sys.argv)

    apply_stylesheet(app,theme="dark_teal.xml")
    # 创建主应用程序窗口
    main_app = MyApp()

    loader = Loader(main_app,1000)
    #loader.loaderUi.show()
    sys.exit(app.exec())