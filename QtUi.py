from PySide6 import QtCore, QtWidgets, QtGui
import matplotlib.pyplot as plt
import functions as fun

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Project 2024")

        ReadFileButton = QtWidgets.QPushButton("Read File")
        CalcBasicButton = QtWidgets.QPushButton("Basic Stats")
        CalcMonthButton = QtWidgets.QPushButton("Month Stats")
        CalcSeasonButton = QtWidgets.QPushButton("Season Stats")
        CalcRoomTypeButton = QtWidgets.QPushButton("Room Type Stats")
        CalcVisitorTypeButton = QtWidgets.QPushButton("Visitor Type Stats")
        CalcTrendButton = QtWidgets.QPushButton("Trends")

        ConsoleText = QtWidgets.QLabel("Please Click Read File To Start." )
        ConsoleText.setStyleSheet("QLabel {color: black; background-color: silver; border: 1px solid gray; border-radius: 2px;}")

        
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
        menuLayout.addWidget(CalcMonthButton)
        menuLayout.addWidget(CalcSeasonButton)
        menuLayout.addWidget(CalcRoomTypeButton)
        menuLayout.addWidget(CalcVisitorTypeButton)
        menuLayout.addWidget(CalcTrendButton)

        menuLayout.insertSpacing(-1,500)
        outerLayout.addLayout(menuLayout)
        outerLayout.addLayout(outputLayout)
        
        def readFileButton_func():
            ConsoleText.setText("Reading File... Please Wait.")
            ConsoleText.repaint()
            QtWidgets.QApplication.processEvents()
            try:
                fun.readFile('hotel_booking.csv')
            except FileNotFoundError:
                ConsoleText.setText("File does not exist!")
            else:
                ConsoleText.setText("File Read Successfully!")

        def calcBasicsButton_func():
            try:
                fun.calcBasics()
            except NameError:
                ConsoleText.setText("No File Selected! Please Read A File First.")
            else:
                ConsoleText.setText("Basic Stats Calculations Successful! Showing Graph.")
                pixmap = QtGui.QPixmap(".basicStats.png")
                pic.setPixmap(pixmap)
                pic.setScaledContents(True)
                pic.show()

        def calcMonthsButton_func():
            try:
                fun.calcMonthStats()
            except NameError:
                ConsoleText.setText("No File Selected! Please Read A File First.")
            else:
                ConsoleText.setText("Month Stats Calculation Successful! Showing Graph.")
                pixmap= QtGui.QPixmap(".monthStats.png")
                pic.setPixmap(pixmap)
                pic.setScaledContents(True)
                pic.show()

        def calcSeasonButton_func():
            try:
                fun.calcSeasonStats()
            except NameError:
                ConsoleText.setText("No File Selected! Please Read A File First.")
            else:
                ConsoleText.setText("Season Stats Calculation Succeessful! Showing Graph.")
                pixmap = QtGui.QPixmap(".seasonStats.png")
                pic.setPixmap(pixmap)
                pic.setScaledContents(True)
                pic.show()

        def calcRoomTypeButton_func():
            try:
                fun.calcRoomTypeStats()
            except NameError:
                ConsoleText.setText("No File Selected! Please Read A File First.")
            else:
                ConsoleText.setText("Room Type Calculation Successful! Showing Graph.")
                pixmap = QtGui.QPixmap(".roomTypeStats.png")
                pic.setPixmap(pixmap)
                pic.setScaledContents(True)
                pic.show()

        def calcVisitorTypeButton_func():
            try:
                fun.calcVisitorTypeStats()
            except NameError:
                ConsoleText.setText("No File Selected! Please Read A File First.")
            else:
                ConsoleText.setText("Visitor Type Stats Calculation Successful! Showing Graph.")
                pixmap = QtGui.QPixmap(".visitorTypeStats.png")
                pic.setPixmap(pixmap)
                pic.setScaledContents(True)
                pic.show()

        def calcTrendButton_func():
            ConsoleText.setText("Calculating Trend... Please Wait.")
            ConsoleText.repaint()
            QtWidgets.QApplication.processEvents()
            try:
                fun.calcTrend()
            except NameError:
                ConsoleText.setText("No File Selected! Please Read A File First.")
            else:
                ConsoleText.setText("Trend Calculation Successful! Showing Graph.")
                pixmap = QtGui.QPixmap(".trend.png")
                pic.setPixmap(pixmap)
                pic.setScaledContents(True)
                pic.show()

        ReadFileButton.clicked.connect(readFileButton_func)
        CalcBasicButton.clicked.connect(calcBasicsButton_func)
        CalcMonthButton.clicked.connect(calcMonthsButton_func)
        CalcSeasonButton.clicked.connect(calcSeasonButton_func)
        CalcRoomTypeButton.clicked.connect(calcRoomTypeButton_func)
        CalcVisitorTypeButton.clicked.connect(calcVisitorTypeButton_func)
        CalcTrendButton.clicked.connect(calcTrendButton_func)
