import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import QSize
import pages as pg
import globaldata as gd


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs) 

        self.setWindowTitle("CSV Quick Edit")
        self.resize(QSize(1000, 600))

        # Stacked widget allows to switch between pages (widgets)
        self.mainwidget = QStackedWidget()
        self.setCentralWidget(self.mainwidget)

        # If user opens the app using "open with"
        if gd.file_path:
            self.firstPageSetup(mark=1)
            self.secondPageSetup(gd.file_path)
        else:
            self.firstPageSetup()


    def firstPageSetup(self, mark=None):
        page1 = pg.FirstPage(self)
        self.mainwidget.addWidget(page1)
        if mark is None:
            self.mainwidget.setCurrentIndex(0)


    def secondPageSetup(self):
        self.page2 = pg.CSVPage(self)
        self.mainwidget.addWidget(self.page2)
        self.mainwidget.setCurrentIndex(1)
    

    def thirdPageSetup(self):
        self.page3 = pg.AnalysisPage(self)
        self.mainwidget.addWidget(self.page3)
        self.mainwidget.setCurrentIndex(2)

    
    def closeEvent(self, event):
        event.accept()
        


#Create and start the app
app = QApplication(sys.argv)

if len(sys.argv) > 1:
        gd.file_path = sys.argv[1]

window = MainWindow()
window.show()

# starts event loop. Using _ because exec is keyword
app.exec_() 
