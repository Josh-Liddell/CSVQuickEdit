from PyQt5.QtGui import * # not best practice 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs) 

        self.setWindowTitle("Text File Analyzer")
        self.setFixedSize(QSize(700, 450)) 
        label = QLabel("Please select a file for analysis")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)





app = QApplication(sys.argv)


window = MainWindow()
window.show() # IMPORTANT

app.exec_() # starts event loop. Using _ because exec is keyword
