import logging
import sys
from time import sleep
from PySide6.QtCore import QMutex, QObject, QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
logging.basicConfig(format="%(message)s", level=logging.INFO)
balance = 100.00 # 账户余额
mutex = QMutex() # 防止 balance 被多个线程同时访问
class AccountManager(QObject):
    finished = Signal() # 结束的信号
    updatedBalance = Signal()
    def withdraw(self, person, amount):
        logging.info("%s wants to withdraw $%.2f...", person, amount)
        global balance
        mutex.lock() # 锁定
        if balance - amount >= 0:
            sleep(1)
            balance -= amount
            logging.info("-$%.2f accepted", amount)
        else:
            logging.info("-$%.2f rejected", amount)
        logging.info("===Balance===: $%.2f", balance)
        self.updatedBalance.emit()
        mutex.unlock() # 解锁
        self.finished.emit()
class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.threads = []
    def setupUi(self):
        """创建 GUI 需要的代码
        """
        self.setWindowTitle("Account Manager")
        self.resize(200, 150)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        button = QPushButton("Withdraw Money!")
        button.clicked.connect(self.startThreads) # 绑定按钮
        self.balanceLabel = QLabel(f"Current Balance: ${balance:,.2f}")
        layout = QVBoxLayout()
        layout.addWidget(self.balanceLabel)
        layout.addWidget(button)
        self.centralWidget.setLayout(layout)
    def updateBalance(self):
        """更新余额的显示
        """
        self.balanceLabel.setText(f"Current Balance: ${balance:,.2f}")
    def createThread(self, person, amount):
        """某一个人开始取钱
        Args:
            person (str): 人名
            amount (float): 取钱的金额
        """
        thread = QThread()
        worker = AccountManager()
        worker.moveToThread(thread)
        thread.started.connect(lambda: worker.withdraw(person, amount)) # 将 start 与 withdraw 连起来
        worker.updatedBalance.connect(self.updateBalance)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        return thread
    def startThreads(self):
        self.threads.clear()
        people = {
            "Alice": 60,
            "Bob": 60,
        }
        self.threads = [self.createThread(person, amount) for person, amount in people.items()] # 为每个人创建一个线程
        for thread in self.threads:
            thread.start() # 开始线程
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())