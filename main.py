from PyQt5.QtGui import * # Fix import
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs) 

        self.setWindowTitle("Text File Analyzer")
        self.setFixedSize(QSize(700, 450))


        self.label = QLabel("Please select a text file for analysis")

        self.fileselect = QPushButton("Browse Files")
        self.fileselect.clicked.connect(self.startButtonClicked)
        self.fileselect.setFixedSize(150, 30)
        

        # --- IN progress ---


        # Layout
        self.layout = QVBoxLayout()
        self.layout.addStretch()
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.fileselect, alignment=Qt.AlignCenter)
        self.layout.addStretch()


        # WHAT is this doing below?

        # Container widget to set the layout
        self.container = QWidget()
        self.container.setLayout(self.layout)

        # Set the container widget as the central widget
        self.setCentralWidget(self.container)

    def startButtonClicked(self):
        print("Button clicked!")
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            print("File "+os.path.basename(file_path)+" successfuly loaded")

    def closeEvent(self, event):
        print("Application closed")
        event.accept()
        


app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT

app.exec_() # starts event loop. Using _ because exec is keyword
