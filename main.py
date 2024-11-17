from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import fileanalysis as fa
import pandas as pd


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs) 

        self.setWindowTitle("CSV Quick Edit")
        self.setFixedSize(QSize(1000, 600))
        # self.resize(QSize(1000, 600))

        # Stacked widget allows to switch between pages (widgets)
        self.mainwidget = QStackedWidget()
        self.setCentralWidget(self.mainwidget)

        # Creates the page and adds them to the stacked widget second page will be added after contents recieved
        self.firstPageSetup()

        # Initially show the first page
        self.mainwidget.setCurrentIndex(0)


    def firstPageSetup(self):
        # Widgets
        label = QLabel("Please select a CSV file to edit")
        font = QFont()
        font.setPointSize(18)
        label.setFont(font)

        fileselect = QPushButton("Browse Files")
        fileselect.clicked.connect(self.startButtonClicked)
        fileselect.setFixedSize(150, 30)
        
        # Layout
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(fileselect, alignment=Qt.AlignCenter)
        # layout.addWidget(self.analyze, alignment=Qt.AlignCenter)
        layout.addStretch()

        # Adding the layout(with the widgets) to a page1 widget
        page1 = QWidget()
        page1.setLayout(layout)

        # Adding the page 1 widget to the main stacked widget
        self.mainwidget.addWidget(page1)


    def secondPageSetup(self):
        
        table = QTableWidget()
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.setMinimumSize(900, 500)
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        table.setRowCount(self.df.shape[0])
        table.setColumnCount(self.df.shape[1]) 
        for row in range(self.df.shape[0]):
            for col in range(self.df.shape[1]):
                table.setItem(row, col, QTableWidgetItem(str(self.df.iat[row, col])))

        def updateDataframe(row, col):
            newValue = table.item(row, col).text()
            self.df.iat[row, col] = newValue

        table.cellChanged.connect(updateDataframe)

        button = QPushButton("Go back")
        button2 = QPushButton("Save and Exit")
        button3 = QPushButton("File Analysis")
        button.clicked.connect(self.backButtonClicked)
        button2.clicked.connect(self.saveButtonClicked)
        button3.clicked.connect(self.analysisButtonClicked)
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

        self.page2 = QWidget()
        self.page2.setLayout(layout)
        self.mainwidget.addWidget(self.page2)
    

    def thirdPageSetup(self):

        label = QLabel(f"There are {fa.numCells(self.df)} cells in the file")
        button = QPushButton("Back")
        button.clicked.connect(self.back2Clicked)
        layout = QVBoxLayout()
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(button, alignment=Qt.AlignCenter)
        
        
        self.page3 = QWidget()
        self.page3.setLayout(layout)
        self.mainwidget.addWidget(self.page3)


    def startButtonClicked(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser("~/Downloads"), "CSV Files (*.csv)")
        if self.file_path:
            
            # Create the pandas dataframe
            self.df = pd.read_csv(self.file_path, dtype="object")
            
            # Here run the file analysis page setup and conduct analysis using the df
            
            self.secondPageSetup()
            self.mainwidget.setCurrentIndex(1)

        else:
            print("Failed to find filepath")


    def backButtonClicked(self):
        self.mainwidget.setCurrentIndex(0)
        self.mainwidget.removeWidget(self.page2) # deletes 2nd page when you go back to home

    def back2Clicked(self):
        self.mainwidget.setCurrentIndex(1)
        self.mainwidget.removeWidget(self.page3)


    def analysisButtonClicked(self):
        self.thirdPageSetup()
        self.mainwidget.setCurrentIndex(2)

    def saveButtonClicked(self):
        self.df.to_csv(self.file_path, index=False)
        QApplication.quit()



    def closeEvent(self, event):
        print("Application closed")
        print(self.df)
        event.accept()
        


#Create and start the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# starts event loop. Using _ because exec is keyword
app.exec_() 
