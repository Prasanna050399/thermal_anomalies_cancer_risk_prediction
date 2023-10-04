from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import HomeScreen
from Cache import Cache
from Database import Database
from json import dumps
from NumpyEncoder import NumpyEncoder

class PatientReportsScreen(object):
    def __init__(self, window):
        window.__init__()
        self.setupUi(window)
        self.cache = Cache()
    
    def setupUi(self, patientReportScreen):
        patientReportScreen.setObjectName("patientReportScreen")
        patientReportScreen.resize(1200, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(patientReportScreen.sizePolicy().hasHeightForWidth())
        patientReportScreen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        patientReportScreen.setFont(font)
        self.centralwidget = QtWidgets.QWidget(patientReportScreen)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
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
        self.patientReportsSection = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.patientReportsSection.setObjectName("patientReportsSection")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.patientReportsSection)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.visitDateField = QtWidgets.QComboBox(self.patientReportsSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visitDateField.sizePolicy().hasHeightForWidth())
        self.visitDateField.setSizePolicy(sizePolicy)
        self.visitDateField.setMinimumSize(QtCore.QSize(400, 0))
        self.visitDateField.setMaximumSize(QtCore.QSize(400, 100))
        self.visitDateField.setObjectName("visitDateField")
        self.gridLayout_4.addWidget(self.visitDateField, 0, 1, 1, 1)
        self.visitDateLabel = QtWidgets.QLabel(self.patientReportsSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visitDateLabel.sizePolicy().hasHeightForWidth())
        self.visitDateLabel.setSizePolicy(sizePolicy)
        self.visitDateLabel.setObjectName("visitDateLabel")
        self.gridLayout_4.addWidget(self.visitDateLabel, 0, 0, 1, 1)
        self.viewReportButton = QtWidgets.QPushButton(self.patientReportsSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewReportButton.sizePolicy().hasHeightForWidth())
        self.viewReportButton.setSizePolicy(sizePolicy)
        self.viewReportButton.setObjectName("viewReportButton")
        self.gridLayout_4.addWidget(self.viewReportButton, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.patientReportsSection, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        patientReportScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(patientReportScreen)
        self.statusbar.setObjectName("statusbar")
        patientReportScreen.setStatusBar(self.statusbar)

        self.retranslateUi(patientReportScreen)
        QtCore.QMetaObject.connectSlotsByName(patientReportScreen)
        
        self.searchMethod = ""
        self.patientResults = []
        self.reportResults = []
        
        self.setupWidgets()
        self.window = patientReportScreen

    def retranslateUi(self, patientReportScreen):
        _translate = QtCore.QCoreApplication.translate
        patientReportScreen.setWindowTitle(_translate("patientReportScreen", "Patient Report Search Screen"))
        self.backButton.setText(_translate("patientReportScreen", "Go back to Main Menu"))
        self.patientSearchSection.setTitle(_translate("patientReportScreen", "Patient Search Section"))
        self.searchQueryLabel.setText(_translate("patientReportScreen", "Search Query"))
        self.selectPatientButton.setText(_translate("patientReportScreen", "Select Patient"))
        self.searchButton.setText(_translate("patientReportScreen", "Search"))
        self.searchMethodLabel.setText(_translate("patientReportScreen", "Search method"))
        self.searchByIdButton.setText(_translate("patientReportScreen", "By Patient ID"))
        self.searchByMobileButton.setText(_translate("patientReportScreen", "By Patient Mobile Number"))
        self.resultsLabel.setText(_translate("patientReportScreen", "Results"))
        self.searchByNameButton.setText(_translate("patientReportScreen", "By Patient Name"))
        self.patientReportsSection.setTitle(_translate("patientReportScreen", "Patient Reports Section"))
        self.visitDateLabel.setText(_translate("patientReportScreen", "Select visit date"))
        self.viewReportButton.setText(_translate("patientReportScreen", "View Report"))
        
    def setupWidgets(self):
        self.backButton.clicked.connect(lambda:self.buttonClicked(self.backButton))
        self.searchByIdButton.clicked.connect(lambda:self.buttonClicked(self.searchByIdButton))
        self.searchByNameButton.clicked.connect(lambda:self.buttonClicked(self.searchByNameButton))
        self.searchByMobileButton.clicked.connect(lambda:self.buttonClicked(self.searchByMobileButton))
        self.searchByNameButton.setChecked(True)
        self.searchMethod = "Name"
        self.searchButton.clicked.connect(lambda:self.buttonClicked(self.searchButton))
        self.selectPatientButton.clicked.connect(lambda:self.buttonClicked(self.selectPatientButton))
        self.viewReportButton.clicked.connect(lambda:self.buttonClicked(self.viewReportButton))
        
    def buttonClicked(self, button):
        if button == self.backButton:
            self.window.close()
            window = self.window
            del self.window
            del self.cache
            self.patientResults.clear()
            del self.patientResults
            self.reportResults.clear()
            del self.reportResults
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
            query = self.searchQueryField.text()
            method = self.searchMethod
            self.patientResults.clear()
            con = Database()
            _ = con.openConnection()
            if _ is True:
                self.patientResults = con.searchInDB(method, query)
                con.closeConnection()
                self.resultsField.clear()
                for entry in self.patientResults:
                    temp = entry[0] + "    " + entry[1] + "    " + entry[2]
                    self.resultsField.addItem(temp)
            else:
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
            idx = self.resultsField.currentIndex()
            if idx != -1:
                patientId = self.patientResults[idx][0]
                con = Database()
                _ = con.openConnection()
                if _ is True:
                    self.cache.setPatientID(patientId)
                    self.reportResults.clear()
                    self.reportResults = con.findPatientVisitDates(patientId)
                    con.closeConnection()
                    self.visitDateField.clear()
                    self.visitDateField.addItems(self.reportResults)
                else:
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
            else:
                failureMsgBox = QMessageBox()
                failureMsgBox.setIcon(QMessageBox.Warning)
                failureMsgBox.setWindowTitle("Invalid Selection")
                failureMsgBox.setText("Patient not selected")
                additionalText = "Please select a valid patient from drop down menu."
                failureMsgBox.setInformativeText(additionalText)
                failureMsgBox.setStandardButtons(QMessageBox.Ok)
                failureMsgBox.exec_()
        elif button == self.viewReportButton:
            idx = self.visitDateField.currentIndex()
            if idx != -1:
                visitDate = self.reportResults[idx]
                con = Database()
                _ = con.openConnection()
                if _ is True:
                    self.cache.setVisitDate(visitDate)
                    temp = con.getPatientVisitDataFromDB(self.cache.id, self.cache.date)
                    con.closeConnection()
                    self.cache.id = temp["PatientID"]
                    self.cache.date = temp["VisitDate"]
                    self.cache.originalImages = temp["OriginalImages"]
                    self.cache.anomalies = temp["AnomalyImages"]
                    self.cache.edges = temp["EdgeImages"]
                    self.cache.diagnosticScore = temp["DiagnosticScore"]
                    self.cache.fullRemarks = temp["Remarks"]
                    '''
                        #Report generation code
                    '''
                    # testing code
                    #print(dumps(temp, cls=NumpyEncoder))
                    print("Patient visit data loaded into memory successfully.")
                    #
                else:
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
            else:
                failureMsgBox = QMessageBox()
                failureMsgBox.setIcon(QMessageBox.Warning)
                failureMsgBox.setWindowTitle("Invalid Selection")
                failureMsgBox.setText("Visit date not selected")
                additionalText = "Please select a valid visit date from drop down menu."
                failureMsgBox.setInformativeText(additionalText)
                failureMsgBox.setStandardButtons(QMessageBox.Ok)
                failureMsgBox.exec_()
        
