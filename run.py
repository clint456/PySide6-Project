
"""
程序入口文件
"""

import sys

from PySide6.QtWidgets import QApplication
from src import loadWin,mainWin
from qt_material import apply_stylesheet



# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme='dark_blue.xml')  
    #mainWin.MainWin().show()
    loadWin.LoadWin().show()   
    app.exec()


