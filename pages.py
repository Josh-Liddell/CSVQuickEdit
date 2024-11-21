from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import pandas as pd
import globaldata as gd

class FirstPage(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Select a CSV file to edit")
        font = QFont()
        font.setPointSize(26)
        label.setFont(font)

        fileselect = QPushButton("Browse Files")
        fileselect.clicked.connect(self.startButtonClicked)
        fileselect.setFixedSize(150, 30)
        fileselect.setStyleSheet("""
        QPushButton {
            background-color: #007bff; 
            border-radius: 15px; 
        }
        QPushButton:hover {
            background-color: #6bbfef;
        }
        QPushButton:pressed {
            background-color: #6bbfef;
        }
        """)
        
        # Layout
        layout = QVBoxLayout()
        layout.addStretch(10)
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        layout.addWidget(fileselect, alignment=Qt.AlignCenter)
        # layout.addWidget(self.analyze, alignment=Qt.AlignCenter)
        layout.addStretch(10)

        # page1.setStyleSheet("QWidget { background-color: lightblue; }")
        self.setLayout(layout)

    def startButtonClicked(self):
        gd.file_path, _ = QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser("~/Downloads"), "CSV Files (*.csv)")
        if gd.file_path:
            
            # Create the pandas dataframe
            gd.df = pd.read_csv(gd.file_path, dtype="object", keep_default_na=False)

            # Convert NaN to None
            gd.df = gd.df.where(pd.notna(gd.df), None)
            
            # Create the second page and set it to the index
            # self.secondPageSetup()
            # self.mainwidget.setCurrentIndex(1)

        else:
            print("Failed to find filepath")





