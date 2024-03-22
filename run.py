
"""
程序入口文件
"""

import sys

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from src.loadWin import LoadWin
from src.mainWin import MainWin



# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme='dark_blue.xml')  
    MainWin().show()

    app.exec()


