# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeScreenWindow(object):
    def setupUi(self, homeScreenWindow):
        homeScreenWindow.setObjectName("homeScreenWindow")
        homeScreenWindow.resize(1200, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(homeScreenWindow.sizePolicy().hasHeightForWidth())
        homeScreenWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        homeScreenWindow.setFont(font)
        homeScreenWindow.setMouseTracking(False)
        homeScreenWindow.setTabletTracking(False)
        homeScreenWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        homeScreenWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(homeScreenWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1180, 555))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.existingPatientWindowButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.existingPatientWindowButton.setGeometry(QtCore.QRect(380, 240, 411, 91))
        self.existingPatientWindowButton.setMouseTracking(False)
        self.existingPatientWindowButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.existingPatientWindowButton.setObjectName("existingPatientWindowButton")
        self.pastReportsWindowButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pastReportsWindowButton.setGeometry(QtCore.QRect(380, 360, 411, 91))
        self.pastReportsWindowButton.setMouseTracking(False)
        self.pastReportsWindowButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pastReportsWindowButton.setObjectName("pastReportsWindowButton")
        self.newPatientWindowButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.newPatientWindowButton.setGeometry(QtCore.QRect(380, 110, 411, 91))
        self.newPatientWindowButton.setMouseTracking(False)
        self.newPatientWindowButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.newPatientWindowButton.setDefault(False)
        self.newPatientWindowButton.setFlat(False)
        self.newPatientWindowButton.setObjectName("newPatientWindowButton")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 1, 1, 1)
        homeScreenWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(homeScreenWindow)
        self.statusbar.setObjectName("statusbar")
        homeScreenWindow.setStatusBar(self.statusbar)

        self.retranslateUi(homeScreenWindow)
        QtCore.QMetaObject.connectSlotsByName(homeScreenWindow)

    def retranslateUi(self, homeScreenWindow):
        _translate = QtCore.QCoreApplication.translate
        homeScreenWindow.setWindowTitle(_translate("homeScreenWindow", "Home Screen"))
        self.existingPatientWindowButton.setText(_translate("homeScreenWindow", "Existing Patient Scan"))
        self.pastReportsWindowButton.setText(_translate("homeScreenWindow", "See Past Reports"))
        self.newPatientWindowButton.setText(_translate("homeScreenWindow", "New Patient Scan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeScreenWindow = QtWidgets.QMainWindow()
    ui = Ui_homeScreenWindow()
    ui.setupUi(homeScreenWindow)
    homeScreenWindow.show()
    sys.exit(app.exec_())