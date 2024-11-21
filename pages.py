from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import pandas as pd
import globaldata as gd

class FirstPage(QWidget):
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_window = main_window
        
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
            
            self.main_window.secondPageSetup()

        else:
            print("Failed to find filepath")


class CSVPage(QWidget):
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_window = main_window

        table = QTableWidget()
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.setMinimumSize(900, 500)
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        table.setRowCount(gd.df.shape[0])
        table.setColumnCount(gd.df.shape[1]) 
        table.setHorizontalHeaderLabels(gd.df.columns.tolist())
        table.setStyleSheet("""
                QTableWidget {
                    /*background-color: #4c6b7f;*/
                    color: white;
                    gridline-color: white;
                }""") 

        # Populate Table
        for row in range(gd.df.shape[0]):
            for col in range(gd.df.shape[1]):
                table.setItem(row, col, QTableWidgetItem(str(gd.df.iat[row, col])))

        # Updates the dataframe with any changes made
        def updateDataframe(row, col):
            newValue = table.item(row, col).text()
            gd.df.iat[row, col] = newValue

        table.cellChanged.connect(updateDataframe)

        button = QPushButton("Go back")
        button2 = QPushButton("Save and Exit")
        button3 = QPushButton("File Analysis")
        button.clicked.connect(self.backButtonClicked)
        button2.clicked.connect(self.saveButtonClicked)
        # button3.clicked.connect(self.analysisButtonClicked)
        button.setMaximumWidth(180)
        button2.setMaximumWidth(180)
        button3.setMaximumWidth(180)

        layout = QVBoxLayout() 
        layout.addWidget(table, alignment=Qt.AlignCenter)

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(4)
        buttonLayout.addWidget(button)
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(button3)
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(button2)
        buttonLayout.addStretch(4)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)


    def backButtonClicked(self):
        self.main_window.mainwidget.setCurrentIndex(0)
        self.main_window.mainwidget.removeWidget(self.main_window.page2)


    # def analysisButtonClicked(self):
    #     self.thirdPageSetup()
    #     self.mainwidget.setCurrentIndex(2)

    def saveButtonClicked(self):
        gd.df.to_csv(gd.file_path, index=False)
        QApplication.quit()


