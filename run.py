
"""
程序入口文件
"""

import sys

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from win.loadWin import LoadWin

# Run
if __name__ == '__main__':
    app = QApplication()
    apply_stylesheet(app,theme='dark_blue.xml')
    load = LoadWin() 
    load.show()
    app.exec()

