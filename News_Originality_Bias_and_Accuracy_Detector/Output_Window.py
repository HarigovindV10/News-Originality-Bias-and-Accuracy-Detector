import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'News Originality Bias and Accuracy detector'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        result=""
        for character in sys.argv[1:]:
            result=result+character+" "
        self.label = QLabel(result, self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        #self.label.setStyleSheet("QLabel {background-color: red;}")

        #self.button = QPushButton("Test", self)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 300, 300)
        #self.layout.addWidget(self.button, 0, 1)

        self.setLayout(self.layout)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
