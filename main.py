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

        # Widgets
        self.label = QLabel("Please select a text file for analysis")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.fileselect = QPushButton("Browse Files")
        self.fileselect.clicked.connect(self.startButtonClicked)
        self.fileselect.setFixedSize(150, 30)
        self.analyze = QPushButton("Analyze File")
        self.analyze.clicked.connect(self.analyzeButtonClicked)
        self.analyze.setFixedSize(150, 30)
        self.analyze.setStyleSheet("""
                    QPushButton {
                        background-color: #0056b3; 
                        color: white; 
                        border: 1px solid transparent; /* Keeps the original border */
                        border-radius: 5px; /* Adjust this value for rounded corners */
                        padding: 5px; /* Add some padding for size consistency */
                    }
                    QPushButton:hover {
                        background-color: #0056b3; /* Darker blue on hover */
                    }
                """)

        self.analyze.setVisible(False)


        # --- IN progress ---


        # Layout
        self.layout = QVBoxLayout()
        self.layout.addStretch()
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.fileselect, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.analyze, alignment=Qt.AlignCenter)
        self.layout.addStretch()


        # WHAT is this doing below?

        # Container widget to set the layout
        self.container = QWidget()
        self.container.setLayout(self.layout)

        # Set the container widget as the central widget
        self.setCentralWidget(self.container)

    def startButtonClicked(self):
        print("Button clicked!")
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser("~/Downloads"), "Text Files (*.txt)")

        if file_path:
            userfile = open(file_path, 'r')
            self.content = userfile.read()
            self.label.setText("File successfully loaded")
            self.fileselect.setText("Select different file")
            self.label.setStyleSheet("color: green;") 
            self.analyze.setText(f"Analyze {os.path.basename(file_path)}")
            self.analyze.setVisible(True)
        else:
            print("Failed to find filepath")
    
    def analyzeButtonClicked(self):
        print("analyzing... Here is the file content: ")
        print(self.content)
    

    def closeEvent(self, event):
        print("Application closed")
        event.accept()
        


app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT

app.exec_() # starts event loop. Using _ because exec is keyword
