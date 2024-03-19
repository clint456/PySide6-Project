from PySide6.QtCore import Signal,QObject
from PySide6.QtWidgets import QApplication, QTextBrowser

# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):

    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    text_print = Signal(str)

    # 还可以定义其他种类的信号
    update_table = Signal(int)