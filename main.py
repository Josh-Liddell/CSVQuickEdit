from PyQt5.QtGui import * # Fix import
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs) 

        self.setWindowTitle("Text File Analyzer")
        self.setFixedSize(QSize(700, 450))

        layout = QVBoxLayout()

        label = QLabel("Please select a file for analysis")

        fileselect = QPushButton("Browse Files")
        fileselect.setFixedSize(150, 30)







        # IN progress

        # Layout
        layout.addStretch()
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(fileselect, alignment=Qt.AlignCenter)
        layout.addStretch()

        # Container widget to set the layout
        container = QWidget()
        container.setLayout(layout)

        # Set the container widget as the central widget
        self.setCentralWidget(container)





app = QApplication(sys.argv)


window = MainWindow()
window.show() # IMPORTANT

app.exec_() # starts event loop. Using _ because exec is keyword
