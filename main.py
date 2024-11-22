from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import fileanalysis as fa
import pandas as pd
import pages as pg


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs) 

        self.setWindowTitle("CSV Quick Edit")
        # self.setFixedSize(QSize(1000, 600))
        self.resize(QSize(1000, 600))

        # Stacked widget allows to switch between pages (widgets)
        self.mainwidget = QStackedWidget()
        self.setCentralWidget(self.mainwidget)

        # Creates the page and adds them to the stacked widget second page will be added after contents recieved
        self.firstPageSetup()

        # Initially show the first page
        self.mainwidget.setCurrentIndex(0)


    def firstPageSetup(self):
        page1 = pg.FirstPage(self)
        self.mainwidget.addWidget(page1)


    def secondPageSetup(self):
        self.page2 = pg.CSVPage(self)
        self.mainwidget.addWidget(self.page2)
        self.mainwidget.setCurrentIndex(1)
    

    def thirdPageSetup(self):
        self.page3 = pg.AnalysisPage(self)
        self.mainwidget.addWidget(self.page3)
        self.mainwidget.setCurrentIndex(2)


    
    def closeEvent(self, event):
        print("Application closed")
        event.accept()
        


#Create and start the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# starts event loop. Using _ because exec is keyword
app.exec_() 
