from PySide6 import QtCore, QtWidgets, QtGui
import matplotlib.pyplot as plt
import functions as fun

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Project 2024")
        ReadFileButton = QtWidgets.QPushButton("ReadFile")
        ReadFileButton.setFixedSize(100,20)
        
        CalcBasicButton = QtWidgets.QPushButton("Basic Stats")
        CalcBasicButton.setFixedSize(100,20)

        ConsoleText = QtWidgets.QLabel("...Console...")

        
        outerLayout = QtWidgets.QHBoxLayout(self) 
        menuLayout = QtWidgets.QVBoxLayout()
        outputLayout = QtWidgets.QVBoxLayout()

        pic = QtWidgets.QLabel(self, alignment=QtCore.Qt.AlignCenter)
        fig= plt.figure()
        fig.savefig(".blank.png")
        pixmap = QtGui.QPixmap(".blank.png")
        pic.setPixmap(pixmap)
        outputLayout.addWidget(pic)
        pic.show()

        outputLayout.addWidget(ConsoleText)
        menuLayout.addWidget(ReadFileButton)
        menuLayout.addWidget(CalcBasicButton)
        outerLayout.addLayout(outputLayout)
        outerLayout.addLayout(menuLayout)
        
        def readFileButton_func():
            ConsoleText.setText("Reading File...")
            ConsoleText.repaint()
            try:
                fun.readFile('hotel_booking.csv')
            except FileNotFoundError:
                ConsoleText.setText("File does not exist!")
            else:
                ConsoleText.setText("File Read Successfully!")

        def calcBasicsButton_func():
            try:
                fun.calcBasics()
            except:
                ConsoleText.setText("No File Selected! Please Read A File First.")
            else:
                ConsoleText.setText("Basic Stats Calculations Successful! Showing Graph.")
                pixmap = QtGui.QPixmap(".basicStats.png")
                pic.setPixmap(pixmap)
                pic.show()

        ReadFileButton.clicked.connect(readFileButton_func)
        CalcBasicButton.clicked.connect(calcBasicsButton_func)
