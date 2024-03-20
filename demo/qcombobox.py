from PySide6.QtWidgets import QApplication, QWidget, QComboBox
 
class Box(QWidget):
    def __init__(self):
        super(Box, self).__init__()
        self.setWindowTitle("QComboBox")
        self.setGeometry(300, 300, 700, 400)
        self.UI()
 
    def UI(self):
        self.com = QComboBox(self)
        self.setGeometry(100, 100, 120, 30)
        self.show()
 
if __name__ == '__main__':
    app = QApplication([])
    box = Box()
    app.exec()