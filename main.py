import pandas as pd
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

def readFile(fileName):
    global csvFile
    df = pd.read_csv(fileName)
    csvFile = df.to_dict(orient='records')

def calcStayInNightsAvg():
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
    resortNightsAvg /= resortCounter
    cityNightsAvg /= cityCounter
    print("Resort Hotel Stay-in Night Average: " + str(resortNightsAvg))
    print("City Hotel Stay-in Night Average: " + str(cityNightsAvg))

def calcCansellationPrc():
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
    resortCancellationPrc = (resortCancellationPrc / resortCounter) * 100
    cityCancellationPrc = (cityCancellationPrc / cityCounter) * 100

    print("Resort Hotel Cansellation Precentage: " + str(resortCancellationPrc) + "%")
    print("City Hotel Cansellation Precentage: " + str(cityCancellationPrc) + "%")

readFile('hotel_booking.csv')
calcStayInNightsAvg()
calcCansellationPrc()

app = QtWidgets.QApplication([])

if __name__ == "__main__":
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    app.exec()
