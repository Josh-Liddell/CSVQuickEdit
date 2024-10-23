from PyQt5.QtGui import * # not best practice I guess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs) # just always have this here I guess not sure what it does entirely

        self.setWindowTitle("My New Window")
        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)





# allows us to pass command line arguments into our application
# sys is important, you can also pass in a empty list if you wont be using command line argumetns
app = QApplication(sys.argv)


window = MainWindow()
window.show() # IMPORTANT

app.exec_() # starts event loop. Using _ because exec is keyword




# Here I will just write my code and be a happy little developer.
