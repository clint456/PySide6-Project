
"""
main_win 测试入口
"""

import sys

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from win.antiDroneWin import AntiDrone



# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme='dark_blue.xml')
    main = AntiDrone()
    main.show()
    # 应用关闭时返回0,sys关闭进程
    sys.exit(app.exec())
