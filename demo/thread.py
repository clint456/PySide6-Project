import sys
import time
from qt_material import apply_stylesheet


from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QObject, Signal, QThread


class Worker(QObject):

    # 数据传输信号
    data_signal = Signal(int)
    # 错误传输信号
    error_signal = Signal(str)
    # 任务结束信号
    finish_signal = Signal()

    def __init__(self):
        super().__init__()

        self.running = False
        self.pause = False

    def work(self):
        self.running = True

        count = 0
        while self.running:
            if self.pause:
                time.sleep(0.1)
                continue
            self.data_signal.emit(count)

            if count == 10:
                try:
                    a = 1/0
                except Exception as e:
                    self.error_signal.emit(str(e))
                    break

            count += 1
            time.sleep(1)

        self.finish_signal.emit()

    def work_stop(self):
        self.running = False

    def work_pause(self):
        self.pause = True

    def work_resume(self):
        self.pause = False


class App(QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        self.resize(600, 490)
        self.title = 'The Window Title'
        self.setWindowTitle(self.title)

        self.label = QLabel()
        self.label.setText('测试')
        self.btn1 = QPushButton()
        self.btn2 = QPushButton()
        self.btn3 = QPushButton()
        self.btn1.setText('启动')
        self.btn2.setText('暂停')
        self.btn3.setText('停止')
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)
        self.btn1.clicked.connect(self.start_thread)
        self.btn2.clicked.connect(self.control_thread)
        self.btn3.clicked.connect(self.stop_thread)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        self.setLayout(layout)

    def start_thread(self):
        # 初始化任务
        self.my_worker = Worker()
        # 初始化线程
        self.my_thread = QThread(self)
        # 将任务添加到线程中
        self.my_worker.moveToThread(self.my_thread)
        # 任务信号处理
        self.my_worker.data_signal.connect(self.on_process_data)
        self.my_worker.error_signal.connect(self.on_error_occurred)
        self.my_worker.finish_signal.connect(self.on_work_finished)
        # 线程信号处理
        self.my_thread.started.connect(self.on_thread_started)
        self.my_thread.started.connect(self.my_worker.work)
        self.my_thread.finished.connect(self.on_thread_finished)
        # 启动线程
        self.my_thread.start()

    def control_thread(self):
        # 线程暂停，恢复
        if self.btn2.text() == "暂停":
            self.my_worker.work_pause()
            self.btn2.setText("继续")
        else:
            self.my_worker.work_resume()
            self.btn2.setText("暂停")

    def stop_thread(self):
        # 停止线程
        self.my_worker.work_stop()

    def on_process_data(self, data):
        # 任务数据处理
        self.label.setText(str(data))

    def on_error_occurred(self, err):
        # 错误处理
        self.label.setText(err)

    def on_work_finished(self):
        # 任务结束，停止线程
        self.my_thread.quit()
        self.my_thread.wait()

    def on_thread_started(self):
        # 线程启动，按钮状态处理
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(True)
        self.btn3.setEnabled(True)

    def on_thread_finished(self):
        # 线程结束，销毁任务和线程实例，释放内存
        self.my_thread.deleteLater()
        self.my_worker.deleteLater()
        # 更新按钮状态
        self.btn1.setEnabled(True)
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme='dark_blue.xml')
    widget = App()
    widget.show()
    sys.exit(app.exec())

