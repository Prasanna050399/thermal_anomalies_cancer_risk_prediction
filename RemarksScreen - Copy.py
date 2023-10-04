from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from json import dumps
from Cache import Cache
from Database import Database
import EdgeDetectionScreen
import HomeScreen
from Prediction import Prediction
from FeatureVector import FeatureVector

class RemarksScreen(object):
    def __init__(self, window, cache=None):
        window.__init__()
        self.cache = cache
        self.setupUi(window)
        #window.showMaximized() ## remove on integration
        
    def setupUi(self, remarksWindow):
        remarksWindow.setObjectName("remarksWindow")
        remarksWindow.resize(1200, 600)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        remarksWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(remarksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -56, 1159, 611))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.backButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.backButton.setObjectName("backButton")
        self.gridLayout_2.addWidget(self.backButton, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.leftBreastRemarks = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.leftBreastRemarks.setObjectName("leftBreastRemarks")
        self.gridLayout_2.addWidget(self.leftBreastRemarks, 2, 3, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_2.addWidget(self.nextButton, 9, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 7, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 6, 0, 1, 1)
        self.suggestRemarks = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.suggestRemarks.setObjectName("suggestRemarks")
        self.gridLayout_2.addWidget(self.suggestRemarks, 6, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem6, 5, 3, 1, 1)
        self.rightBreastRemarks = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.rightBreastRemarks.setObjectName("rightBreastRemarks")
        self.gridLayout_2.addWidget(self.rightBreastRemarks, 4, 3, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 8, 1, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        remarksWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(remarksWindow)
        self.statusbar.setObjectName("statusbar")
        remarksWindow.setStatusBar(self.statusbar)

        self.retranslateUi(remarksWindow)
        QtCore.QMetaObject.connectSlotsByName(remarksWindow)

        self.window = remarksWindow
        self.downloadCache()
        self.setupWidgets()

    def retranslateUi(self, remarksWindow):
        _translate = QtCore.QCoreApplication.translate
        remarksWindow.setWindowTitle(_translate("remarksWindow", "Remarks of Radiologists"))
        self.backButton.setText(_translate("remarksWindow", "Back"))
        self.label.setText(_translate("remarksWindow", "Impression by Radiologists"))
        self.nextButton.setText(_translate("remarksWindow", "Proceed to Report Generation"))
        self.label_2.setText(_translate("remarksWindow", "Left Breast"))
        self.label_4.setText(_translate("remarksWindow", "Suggest"))
        self.label_3.setText(_translate("remarksWindow", "Right Breast"))

    def setupWidgets(self):
        self.backButton.clicked.connect(lambda:self.buttonClicked(self.backButton))
        self.nextButton.clicked.connect(lambda:self.buttonClicked(self.nextButton))
        self.rightBreastRemarks.textChanged.connect(self.uploadCache)
        self.leftBreastRemarks.textChanged.connect(self.uploadCache)
        self.suggestRemarks.textChanged.connect(self.uploadCache)
        self.progressBar.setEnabled(False)

    def blockAll(self):
        self.backButton.setEnabled(False)
        self.nextButton.setEnabled(False)

    def unblockAll(self):
        self.backButton.setEnabled(True)
        self.nextButton.setEnabled(True)

    def downloadCache(self):
        print(self.cache.remarks)
        self.rightBreastRemarks.setText(self.cache.remarks[0])
        self.leftBreastRemarks.setText(self.cache.remarks[1])
        self.suggestRemarks.setText(self.cache.remarks[2])

    def uploadCache(self):
        self.cache.remarks[0] = self.rightBreastRemarks.toPlainText()
        self.cache.remarks[1] = self.leftBreastRemarks.toPlainText()
        self.cache.remarks[2] = self.suggestRemarks.toPlainText()

    def buttonClicked(self, button):
        if button == self.backButton:
            self.window.close()
            window = self.window
            cache = self.cache
            del self.window
            del self.cache
            obj = EdgeDetectionScreen.EdgeDetectionScreen(window, cache)
            window.showMaximized()
            obj.preprocessScreen()
        elif button == self.nextButton:
            self.blockAll()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Request Confirmation")
            msgBox.setText("Are you sure you want to continue to generate report?")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.proceed()
            else:
                self.unblockAll()
        
    def proceed(self):
        self.progressBar.setEnabled(True)
        featureVectorGenerator = FeatureVector()
        vec = featureVectorGenerator.Features(self.cache.originalImages[0].copy())
        self.progressBar.setValue(25)
        nn = Prediction()
        res = nn.predict(vec)
        self.progressBar.setValue(50)
        self.cache.nn = res
        #self.cache.nn = ["Negative Breast Mass Characteristics", "82.45"] ##
        self.cache.print() ## remove on integration
        edges = []
        for i in range(len(self.cache.edges)):
            edges.append(self.cache.edges[i][0])
        arr = {
            "PatientID" : self.cache.id,
            "VisitDate" : self.cache.date,
            "VisitTime" : self.cache.time,
            "OriginalImages" : self.cache.originalImages,
            "AnomalyImages" : self.cache.anomalies,
            "EdgeImages" : edges,
            "AsymmetryImage" : self.cache.asymmetryImage,
            "DiagnosticScore" : self.cache.diagnosticScore,
            "Remarks" : self.cache.remarks,
            "DiagnosticMeterFields" : self.cache.diagnosticFields,
            "NN" : self.cache.nn
        }
        con = Database()
        if con.openConnection() is True:
            con.savePatientVisitDataInDB(arr)
            con.closeConnection()
            self.progressBar.setValue(75)
            successMsgBox = QMessageBox()
            successMsgBox.setIcon(QMessageBox.Information)
            successMsgBox.setWindowTitle("Save Successful")
            successMsgBox.setText("Patient scan save successful")
            additionalText = "Patient id. - " + arr["PatientID"] + " scan data saved successfully."
            successMsgBox.setInformativeText(additionalText)
            '''
            new = []
            for image in arr["OriginalImages"]:
                new.append(image.tolist())
            arr["OriginalImages"] = new
            new = []
            for image in arr["AnomalyImages"]:
                new.append(image.tolist())
            arr["AnomalyImages"] = new
            new = []
            for image in arr["EdgeImages"]:
                new.append(image.tolist())
            arr["EdgeImages"] = new
            arr["AsymmetryImage"] = arr["AsymmetryImage"].tolist()
            '''
            #detailedText = dumps(arr)
            #successMsgBox.setDetailedText(detailedText)
            successMsgBox.setStandardButtons(QMessageBox.Ok)
            successMsgBox.exec_()
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
            self.progressBar.setEnabled(False)
            self.unblockAll()
            return
        '''
            TODO : report generation using self.cache
        '''
        self.progressBar.setValue(100)
        self.window.close()
        window = self.window
        del self.window
        del self.cache
        HomeScreen.HomeScreen(window)
        window.showMaximized()


##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    remarksWindow = QtWidgets.QMainWindow()
##    cache = Cache()
##    cache.id = "2021-05-07,23:59:02.527544"
##    cache.isNew = False
##    cache.diagnosticScore = 56
##    cache.diagnosticFields = [0, 0, 0, 0, 0, 0, 0, 0, 0]
##    import cv2 as cv
##    img = cv.imread("thermal_image.jpg")
##    img = cv.resize(img, (640, 480), interpolation = cv.INTER_LANCZOS4)
##    for i in range(5):
##        cache.originalImages[i] = img
##    for i in range(5):
##        cache.anomalies[i] = img
##    for i in range(5):
##        cache.edges[i] = img
##    cache.asymmetryImage = img
##    cache.remarks[0] = "right breast ok"
##    cache.remarks[1] = "left breast wrong"
##    cache.remarks[2] = "no risk"
##    ui = RemarksScreen(remarksWindow, cache)
##    #ui.setupUi(remarksWindow)
##    remarksWindow.show()
##    sys.exit(app.exec_())

