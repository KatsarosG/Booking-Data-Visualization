import pandas as pd
import sys
import matplotlib.pyplot as plt
from PySide6 import QtCore, QtWidgets, QtGui

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
                readFile('hotel_booking.csv')
            except FileNotFoundError:
                ConsoleText.setText("File does not exist!")
            else:
                ConsoleText.setText("File Read Successfully!")

        def calcBasicsButton_func():
            try:
                calcBasics()
            except:
                ConsoleText.setText("No File Selected! Please Read A File First.")
            else:
                ConsoleText.setText("Basic Stats Calculations Successful! Showing Graph.")
                pixmap = QtGui.QPixmap(".basicStats.png")
                pic.setPixmap(pixmap)
                pic.show()

        ReadFileButton.clicked.connect(readFileButton_func)
        CalcBasicButton.clicked.connect(calcBasicsButton_func)

def readFile(fileName):
    global csvFile
    df = pd.read_csv(fileName)
    csvFile = df.to_dict(orient='records')

def calcStayInNightsAvg():
    global resortNightsAvg
    global cityNightsAvg
    resortNightsAvg = 0
    cityNightsAvg = 0
    resortCounter = 0
    cityCounter = 0
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            resortNightsAvg += int(lines['stays_in_weekend_nights']) + int(lines['stays_in_week_nights'])
            resortCounter += 1
        else:
            cityNightsAvg += int(lines['stays_in_weekend_nights']) + int(lines['stays_in_week_nights'])
            cityCounter += 1
    resortNightsAvg = round(resortNightsAvg/resortCounter, 2)
    cityNightsAvg = round(cityNightsAvg/cityCounter, 2)

def calcCansellationPrc():
    global resortCancellationPrc
    global cityCancellationPrc
    resortCancellationPrc = 0
    cityCancellationPrc = 0
    resortCounter = 0
    cityCounter = 0
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            resortCancellationPrc += int(lines['is_canceled'])
            resortCounter += 1
        else:
            cityCancellationPrc += int(lines['is_canceled'])
            cityCounter += 1
    resortCancellationPrc = round(float((resortCancellationPrc / resortCounter) * 100), 2)
    cityCancellationPrc = round(float((cityCancellationPrc / cityCounter) * 100), 2)

def calcBasics():
        calcStayInNightsAvg()
        calcCansellationPrc()

        fig = plt.figure()
        axes = fig.subplots(2)
        axes[0].barh(["Resort", "City"], [resortCancellationPrc, cityCancellationPrc], color=['tab:orange', 'tab:red'])
        axes[0].text(resortCancellationPrc/2, 0, str(resortCancellationPrc) + "%", color = 'white')
        axes[0].text(cityCancellationPrc/2, 1, str(cityCancellationPrc) + "%", color = 'white')
        axes[0].title.set_text("Hotel Cancellation Precentage:")

        axes[1].barh(["Resort", "City"], [resortNightsAvg, cityNightsAvg], color=['tab:orange', 'tab:red'])
        axes[1].text(resortNightsAvg/2, 0, str(resortNightsAvg), color = 'white')
        axes[1].text(cityNightsAvg/2, 1, str(cityNightsAvg), color = 'white')
        axes[1].title.set_text("Hotel Night Stay-Ins Average:")
        fig.tight_layout()
        fig.savefig(".basicStats.png")

app = QtWidgets.QApplication([])

if __name__ == "__main__":
    widget = MyWidget()
    widget.setFixedSize(800, 600)
    widget.show()
    sys.exit(app.exec())
