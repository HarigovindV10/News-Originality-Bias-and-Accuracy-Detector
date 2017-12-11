import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import os

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'News Originality Bias and Accuracy detector'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(260, 280)
        self.textbox.resize(280,40)

        # Create a button in the window
        self.button = QPushButton('Submit', self)
        self.button.move(350,350)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        os.system("python News_Originality_Bias_and_Accuracy_Detector.py "+textboxValue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
