from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Minesweeper")
        self.setFixedSize(QSize(500,500))
        
        button = QPushButton("button")
        
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()
