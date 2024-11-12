from PyQt5.QtGui import * # Fix import
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import fileanalysis as fa


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs) 

        self.setWindowTitle("CSV Quick Edit")
        self.setFixedSize(QSize(1000, 600))
        # self.resize(QSize(1000, 600))

        # USE a STACKED WIDGET because it will allow me to switch between pages (widgets)
        self.mainwidget = QStackedWidget()
        self.setCentralWidget(self.mainwidget)

        # Creates the page and adds them to the stacked widget second page will be added after contents recieved
        self.firstPageSetup()

        # Initially show the first page
        self.mainwidget.setCurrentIndex(0)


    def firstPageSetup(self):
        # Widgets
        self.label = QLabel("Please select a CSV file to edit")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.fileselect = QPushButton("Browse Files")
        self.fileselect.clicked.connect(self.startButtonClicked)
        self.fileselect.setFixedSize(150, 30)
        
        # self.analyze = QPushButton("Analyze File")
        # self.analyze.clicked.connect(self.analyzeButtonClicked)
        # self.analyze.setFixedSize(150, 30)
        # self.analyze.setStyleSheet("""
        #             QPushButton {
        #                 background-color: #0056b3; 
        #                 color: white; 
        #                 border: 1px solid transparent; /* Keeps the original border */
        #                 border-radius: 5px; /* Adjust this value for rounded corners */
        #                 padding: 5px; /* Add some padding for size consistency */
        #             }
        #             QPushButton:hover {
        #                 background-color: #0056b3; /* Darker blue on hover */
        #             }
        #         """)

        # self.analyze.setVisible(False)


        # Layout
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.fileselect, alignment=Qt.AlignCenter)
        # layout.addWidget(self.analyze, alignment=Qt.AlignCenter)
        layout.addStretch()

        # Adding the layout(with the widgets) to a page1 widget
        page1 = QWidget()
        page1.setLayout(layout)

        # Adding the page 1 widget to the main stacked widget
        self.mainwidget.addWidget(page1)

    def secondPageSetup(self):
        
#         wordCt = fa.wordCount(self.content)
#         charCt = fa.numCharacters(self.content)
#         populrWrds = fa.mostPopular(self.content)
        
#         label = QLabel(f"""Words in file: {wordCt}
# Characters in file: {charCt}\n
# Most frequent word: {populrWrds[0][0]} ({populrWrds[0][1]} occurences)
# Second most frequent word: {populrWrds[1][0]} ({populrWrds[1][1]} occurences)
# Third most frequent word: {populrWrds[2][0]} ({populrWrds[2][1]} occurences)""")
        
        table = QTableWidget(10,10)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.setMinimumSize(900, 500)
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        button = QPushButton("Go back")
        button.clicked.connect(self.backButtonClicked)



        layout = QVBoxLayout() 
        # layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(table, alignment=Qt.AlignCenter)
        layout.addWidget(button, alignment=Qt.AlignCenter)
        
        self.page2 = QWidget()
        self.page2.setLayout(layout)
        self.mainwidget.addWidget(self.page2)


    def startButtonClicked(self):
        print("Button clicked!")
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser("~/Downloads"), "CSV Files (*.csv)")
        if self.file_path:
            self.secondPageSetup()
            self.mainwidget.setCurrentIndex(1)
            # self.label.setText("File successfully loaded")
            # self.fileselect.setText("Select different file")
            # self.label.setStyleSheet("color: green;") 
            # self.analyze.setText(f"Analyze {os.path.basename(self.file_path)}")
            # self.analyze.setVisible(True)
        else:
            print("Failed to find filepath")
        
    def analyzeButtonClicked(self):
        userfile = open(self.file_path, 'r')
        self.content = userfile.read()
            
        # print("analyzing... Here is the file content: ")
        # print(self.content)
    
    def backButtonClicked(self):
        self.mainwidget.setCurrentIndex(0)
        self.mainwidget.removeWidget(self.page2) # deletes 2nd page when you go back to home 

    def closeEvent(self, event):
        print("Application closed")
        event.accept()
        


#Create and start the app

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT

app.exec_() # starts event loop. Using _ because exec is keyword
