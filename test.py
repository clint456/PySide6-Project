from PySide6.QtWidgets import QApplication
from thr.mainWinThread import mainWinThread



if __name__ == "__main__":
    app = QApplication()
    main = mainWinThread()
    main.myStart()
    app.exec()