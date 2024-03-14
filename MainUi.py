from loader import Loader

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile,QTimer
from PySide6.QtWebEngineWidgets import QWebEngineView
from qt_material import apply_stylesheet,add_fonts


import sys

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.init_ui()
        

    def init_ui(self):
        # 创建主窗口内容
        self.setWindowTitle('Main Application')
        loader = QUiLoader()

        # 动态加载ui文件
        ui_file_name = "./ui/mainUi.ui"
        ui_file = QFile(ui_file_name)
        ui_file.open(QFile.ReadOnly)

        # 从UI定义中 创建一个相应的窗口对象
        self.loaderUi = loader.load(ui_file)
        ui_file.close()
        # 设置初始启动位置

        self.loaderUi.setParent(self)
        self.loaderUi.setGeometry(100, 100, 400, 400)
        
        #self.loaderUi.pushButton.clicked.connect(lambda:print("按钮按下了"))
        #TODO
        # 在这里可以添加主窗口的其他组件和功能

    def web_engine_init(self):
        self.loaderUi.webEngineView = QWebEngineView(self)# 浏览器控件
        #self.loaderUi.webEngineView.

    def showUi(self):
        self.loaderUi.show()

if __name__ == "__main__":
    # 创建应用程序
    app = QApplication(sys.argv)
    # 使用主题
    apply_stylesheet(app,theme='light_blue.xml')

    # 创建主应用程序窗口
    main_app = MyApp()

    # 使用加载器(<主窗口>,<加载时间>)
    loader = Loader(main_app=main_app,load_time=100)
    main_app.show()
    app.exec()