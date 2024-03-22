
"""
程序入口文件
"""

import sys

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from win.loadWin import LoadWin
from win.mainWin import MainWin



# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme='dark_blue.xml')
    main = MainWin()
    main.show()
    # 应用关闭时返回0,sys关闭进程
    sys.exit(app.exec())
