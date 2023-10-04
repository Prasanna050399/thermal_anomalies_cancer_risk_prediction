from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import HomeScreen
import PatientDataScreen
from Cache import Cache
from Database import Database

class PatientSearchScreen(object):
    def __init__(self, window):
        window.__init__()
        self.setupUi(window)
        self.cache = Cache()
    
    def setupUi(self, patientSearchWindow):
        patientSearchWindow.setObjectName("patientSearchWindow")
        patientSearchWindow.resize(1200, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(patientSearchWindow.sizePolicy().hasHeightForWidth())
        patientSearchWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        patientSearchWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(patientSearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1180, 555))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.backButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setObjectName("backButton")
        self.gridLayout_2.addWidget(self.backButton, 0, 0, 1, 1)
        self.patientSearchSection = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patientSearchSection.sizePolicy().hasHeightForWidth())
        self.patientSearchSection.setSizePolicy(sizePolicy)
        self.patientSearchSection.setObjectName("patientSearchSection")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.patientSearchSection)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.searchQueryLabel = QtWidgets.QLabel(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchQueryLabel.sizePolicy().hasHeightForWidth())
        self.searchQueryLabel.setSizePolicy(sizePolicy)
        self.searchQueryLabel.setObjectName("searchQueryLabel")
        self.gridLayout_3.addWidget(self.searchQueryLabel, 1, 0, 1, 1)
        self.selectPatientButton = QtWidgets.QPushButton(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectPatientButton.sizePolicy().hasHeightForWidth())
        self.selectPatientButton.setSizePolicy(sizePolicy)
        self.selectPatientButton.setObjectName("selectPatientButton")
        self.gridLayout_3.addWidget(self.selectPatientButton, 2, 3, 1, 1)
        self.resultsField = QtWidgets.QComboBox(self.patientSearchSection)
        self.resultsField.setObjectName("resultsField")
        self.gridLayout_3.addWidget(self.resultsField, 2, 1, 1, 2)
        self.searchButton = QtWidgets.QPushButton(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_3.addWidget(self.searchButton, 1, 3, 1, 1)
        self.searchMethodLabel = QtWidgets.QLabel(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchMethodLabel.sizePolicy().hasHeightForWidth())
        self.searchMethodLabel.setSizePolicy(sizePolicy)
        self.searchMethodLabel.setObjectName("searchMethodLabel")
        self.gridLayout_3.addWidget(self.searchMethodLabel, 0, 0, 1, 1)
        self.searchQueryField = QtWidgets.QLineEdit(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchQueryField.sizePolicy().hasHeightForWidth())
        self.searchQueryField.setSizePolicy(sizePolicy)
        self.searchQueryField.setObjectName("searchQueryField")
        self.gridLayout_3.addWidget(self.searchQueryField, 1, 1, 1, 2)
        self.searchByIdButton = QtWidgets.QRadioButton(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchByIdButton.sizePolicy().hasHeightForWidth())
        self.searchByIdButton.setSizePolicy(sizePolicy)
        self.searchByIdButton.setObjectName("searchByIdButton")
        self.gridLayout_3.addWidget(self.searchByIdButton, 0, 1, 1, 1)
        self.searchByMobileButton = QtWidgets.QRadioButton(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchByMobileButton.sizePolicy().hasHeightForWidth())
        self.searchByMobileButton.setSizePolicy(sizePolicy)
        self.searchByMobileButton.setObjectName("searchByMobileButton")
        self.gridLayout_3.addWidget(self.searchByMobileButton, 0, 3, 1, 1)
        self.resultsLabel = QtWidgets.QLabel(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsLabel.sizePolicy().hasHeightForWidth())
        self.resultsLabel.setSizePolicy(sizePolicy)
        self.resultsLabel.setObjectName("resultsLabel")
        self.gridLayout_3.addWidget(self.resultsLabel, 2, 0, 1, 1)
        self.searchByNameButton = QtWidgets.QRadioButton(self.patientSearchSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchByNameButton.sizePolicy().hasHeightForWidth())
        self.searchByNameButton.setSizePolicy(sizePolicy)
        self.searchByNameButton.setObjectName("searchByNameButton")
        self.gridLayout_3.addWidget(self.searchByNameButton, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.patientSearchSection, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        patientSearchWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(patientSearchWindow)
        self.statusbar.setObjectName("statusbar")
        patientSearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(patientSearchWindow)
        QtCore.QMetaObject.connectSlotsByName(patientSearchWindow)
        
        self.searchMethod = ""
        self.results = []
        
        self.setupWidgets()
        self.window = patientSearchWindow

    def retranslateUi(self, patientSearchWindow):
        _translate = QtCore.QCoreApplication.translate
        patientSearchWindow.setWindowTitle(_translate("patientSearchWindow", "Patient Search Screen"))
        self.backButton.setText(_translate("patientSearchWindow", "Go back to Main Menu"))
        self.patientSearchSection.setTitle(_translate("patientSearchWindow", "Patient Search Section"))
        self.searchQueryLabel.setText(_translate("patientSearchWindow", "Search Query"))
        self.selectPatientButton.setText(_translate("patientSearchWindow", "Select Patient"))
        self.searchButton.setText(_translate("patientSearchWindow", "Search"))
        self.searchMethodLabel.setText(_translate("patientSearchWindow", "Search method"))
        self.searchByIdButton.setText(_translate("patientSearchWindow", "By Patient ID"))
        self.searchByMobileButton.setText(_translate("patientSearchWindow", "By Patient Mobile Number"))
        self.resultsLabel.setText(_translate("patientSearchWindow", "Results"))
        self.searchByNameButton.setText(_translate("patientSearchWindow", "By Patient Name"))
        
    def setupWidgets(self):
        self.backButton.clicked.connect(lambda:self.buttonClicked(self.backButton))
        self.searchByIdButton.clicked.connect(lambda:self.buttonClicked(self.searchByIdButton))
        self.searchByNameButton.clicked.connect(lambda:self.buttonClicked(self.searchByNameButton))
        self.searchByMobileButton.clicked.connect(lambda:self.buttonClicked(self.searchByMobileButton))
        self.searchByNameButton.setChecked(True)
        self.searchMethod = "Name"
        self.searchButton.clicked.connect(lambda:self.buttonClicked(self.searchButton))
        self.selectPatientButton.clicked.connect(lambda:self.buttonClicked(self.selectPatientButton))

    def blockAll(self):
        self.backButton.setEnabled(False)
        self.searchByIdButton.setEnabled(False)
        self.searchByNameButton.setEnabled(False)
        self.searchByMobileButton.setEnabled(False)
        self.searchButton.setEnabled(False)
        self.selectPatientButton.setEnabled(False)

    def unblockAll(self):
        self.backButton.setEnabled(True)
        self.searchByIdButton.setEnabled(True)
        self.searchByNameButton.setEnabled(True)
        self.searchByMobileButton.setEnabled(True)
        self.searchButton.setEnabled(True)
        self.selectPatientButton.setEnabled(True)
        
    def buttonClicked(self, button):
        if button == self.backButton:
            self.window.close()
            window = self.window
            del self.window
            del self.cache
            self.results.clear()
            del self.results
            HomeScreen.HomeScreen(window)
            #window.show()
            window.showMaximized()
        elif button == self.searchByIdButton:
            self.searchMethod = "_id"
        elif button == self.searchByNameButton:
            self.searchMethod = "Name"
        elif button == self.searchByMobileButton:
            self.searchMethod = "MobileNo"
        elif button == self.searchButton:
            self.blockAll()
            query = self.searchQueryField.text()
            method = self.searchMethod
            self.results.clear()
            con = Database()
            _ = con.openConnection()
            if _ is True:
                self.results = con.searchInDB(method, query)
                con.closeConnection()
                self.resultsField.clear()
                for entry in self.results:
                    temp = entry[0] + "    " + entry[1] + "    " + entry[2]
                    self.resultsField.addItem(temp)
                self.unblockAll()
            else:
                self.unblockAll()
                failureMsgBox = QMessageBox()
                failureMsgBox.setIcon(QMessageBox.Critical)
                failureMsgBox.setWindowTitle("Database Error")
                failureMsgBox.setText("Connection to database failed")
                additionalText = "Connection to database failed as no running instance of database server found."
                failureMsgBox.setInformativeText(additionalText)
                detailedText = "Application tried to connect to MongoDB Server but failed as no running instance of server was found.\nWhat can be done:\n\t1. Close the application.\n\t2. Look for MongoDB server service \n\t   and start it or manually go to \n\t   MongoDB program files and run \n\t   'mongod.exe' to start service \n\t   with appropriate arguments."
                failureMsgBox.setDetailedText(detailedText)
                failureMsgBox.setStandardButtons(QMessageBox.Ok)
                failureMsgBox.exec_()
        elif button == self.selectPatientButton:
            self.blockAll()
            idx = self.resultsField.currentIndex()
            if idx != -1:
                self.cache.setPatientID(self.results[idx][0])
                self.unblockAll()
                self.window.close()
                window = self.window
                cache = self.cache
                del self.window
                del self.cache
                self.results.clear()
                del self.results
                PatientDataScreen.PatientDataScreen(window, cache=cache)
                window.showMaximized()
            else:
                self.unblockAll()
                failureMsgBox = QMessageBox()
                failureMsgBox.setIcon(QMessageBox.Warning)
                failureMsgBox.setWindowTitle("Invalid Selection")
                failureMsgBox.setText("Patient not selected")
                additionalText = "Please select a valid patient from drop down menu."
                failureMsgBox.setInformativeText(additionalText)
                failureMsgBox.setStandardButtons(QMessageBox.Ok)
                failureMsgBox.exec_()
        
