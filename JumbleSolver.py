from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPixmap
import sys

from dictpro import Dictionary_

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        #load the ui file
        uic.loadUi("jumble.ui", self)
        
        #define our widgets
        self.output=''
        self.search = self.findChild(QPushButton, "SearchBox")
        self.exit = self.findChild(QPushButton, "Exit")
        self.word = self.findChild(QLineEdit, "DictWord")
        self.answer = self.findChild(QLabel, "DictAnswer")
        self.picture = self.findChild(QLabel, "image")
        
        #Function of the widget when clicked
        self.search.clicked.connect(self.dictionary)
        self.exit.clicked.connect(lambda:self.close())

        #show the appe
        filename = "bg.jpg"

        #Open the image
        self.pixmap = QPixmap(filename)
        #Add Pic to the Label
        self.picture.setPixmap(self.pixmap)
        self.show()
        
    def dictionary(self):

        if self.output != '':
            a=self.output
        else:
            a=self.word.text()
        dic=Dictionary_()
        self.output =dic.jumble_solver(a)
        print(self.output)
        var=''
        if type(self.output) == list:
            var='\n'.join(self.output)
            self.output=''
            if var:
                self.answer.setText(var)
            else:
                self.answer.setText("No words found in the dictionary. Sorry!")
                
        else:
            self.answer.setText('')
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText(self.output)
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            self.output=''
            

app = QApplication(sys.argv)
UIWindow = MainWindow()
UIWindow.setWindowTitle("Three-Letter Jumbler")
app.exec_()