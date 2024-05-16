# The main code file that just calls the PyQt Application

import sys
from PySide6 import QtCore, QtWidgets, QtGui

import QtUi as ui
import functions as fun

app = QtWidgets.QApplication([])

if __name__ == "__main__":
    widget = ui.MyWidget()
    widget.setFixedSize(800, 600)
    widget.show()
    sys.exit(app.exec())
