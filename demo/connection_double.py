#coding=GBK
from PySide6.QtWidgets import QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout
from PySide6.QtCore import Signal,Qt
 
class MyWindow(QWidget):
    sendvaluetochild = Signal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle('farther')
        self.mylayout = QVBoxLayout()
        self.line = QLineEdit()
        self.btn = QPushButton('send to kid')
        self.mylayout.addWidget(self.line)
        self.mylayout.addWidget(self.btn)
        self.setLayout(self.mylayout)
        self.bind()
 
    def bind(self):
        self.sub_window = subwindow(self)
        self.sub_window.show()
        self.sub_window.bind()
        self.sendvaluetochild.connect(self.sub_window.edit.setText)
        self.btn.clicked.connect(self.sendvalue)
 
    def sendvalue(self):
        text = self.line.text()
        self.sendvaluetochild.emit(text)
 
 
class subwindow(QWidget):
    sendvaluetoparent = Signal(str)
    def __init__(self,parent=None):
        super().__init__()
        self.move(50,50)
        self.setWindowTitle('kid')
        self.parent = parent
        self.sublayout = QVBoxLayout()
        self.btn1 = QPushButton('send to farther')
        self.edit = QLineEdit()
        self.sublayout.addWidget(self.btn1)
        self.sublayout.addWidget(self.edit)
        self.setLayout(self.sublayout)
    def bind(self):
        self.sendvaluetoparent.connect(self.parent.line.setText)
        self.btn1.clicked.connect(self.sendvalue)
    def sendvalue(self):
        self.sendvaluetoparent.emit(self.edit.text())
 
 
 
if __name__=='__main__':
    app=QApplication()
    Window = MyWindow()
    Window.show()
    app.exec() 