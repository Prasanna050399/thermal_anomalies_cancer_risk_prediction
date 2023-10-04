import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import HomeScreen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = HomeScreen.HomeScreen(window)
    #window.show()
    window.showMaximized()
    sys.exit(app.exec_())
