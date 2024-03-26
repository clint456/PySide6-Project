from PySide6.QtCore import QThread, QObject, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton

class LongProcessThread(QThread):
    """长时间进程线程类"""

    process_signal = Signal(str)  # 信号：发送进程信息

    def run(self):
        """长时间进程代码"""
        for i in range(1, 6):
            self.process_signal.emit(f"进程{i}")  # 发送进程信息
            self.sleep(1)  # 暂停1秒

class ConcurrentInfoWindow(QDialog):
    """并发信息窗口类"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("并发信息")
        self.resize(300, 200)

        layout = QVBoxLayout(self)
        self.info_label = QLabel(self)
        layout.addWidget(self.info_label)

        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(lambda: self.show_info("等待结束"))
        timer.start(3000)  # 设定延迟3秒，过期触发timeout信号

    def show_info(self, info: str):
        """显示进程信息"""
        self.info_label.setText(info)

class MainWindow(QMainWindow):
    """主窗口类"""

    def __init__(self):
        super().__init__()

        button = QPushButton("启动长时间进程", self)
        button.clicked.connect(self.start_long_process)
        self.setCentralWidget(button)

        self.concurrent_window = ConcurrentInfoWindow(self)

        self.thread = LongProcessThread(self)
        self.thread.process_signal.connect(self.show_process_info)  # 接收进程信息信
        
        
if __name__ == "__main___":
    app = QApplication()
    MainWindow().show()
    app.exec()