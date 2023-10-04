from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread
from Cache import Cache
from Image import imageConversion, showOnWidget
import ImageSelectionScreen
import EdgeDetectionScreen

class AnomalyDetectionScreen(object):
    def __init__(self, window, cache=None):
        window.__init__()
        self.cache = cache
        self.setupUi(window)
        #window.showMaximized() ## remove on integration
        
    def setupUi(self, anomalyDetectionWindow):
        anomalyDetectionWindow.setObjectName("anomalyDetectionWindow")
        anomalyDetectionWindow.resize(1200, 600)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        anomalyDetectionWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(anomalyDetectionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1330, 1831))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 9, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 4, 2, 1, 1)
        self.leftObliqueViewAnomalyImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftObliqueViewAnomalyImageLabel.sizePolicy().hasHeightForWidth())
        self.leftObliqueViewAnomalyImageLabel.setSizePolicy(sizePolicy)
        self.leftObliqueViewAnomalyImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.leftObliqueViewAnomalyImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.leftObliqueViewAnomalyImageLabel.setText("")
        self.leftObliqueViewAnomalyImageLabel.setObjectName("leftObliqueViewAnomalyImageLabel")
        self.gridLayout_2.addWidget(self.leftObliqueViewAnomalyImageLabel, 13, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 9, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 14, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 15, 0, 1, 3)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 10, 0, 1, 1)
        self.rightObliqueViewAnomalyImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightObliqueViewAnomalyImageLabel.sizePolicy().hasHeightForWidth())
        self.rightObliqueViewAnomalyImageLabel.setSizePolicy(sizePolicy)
        self.rightObliqueViewAnomalyImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.rightObliqueViewAnomalyImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.rightObliqueViewAnomalyImageLabel.setText("")
        self.rightObliqueViewAnomalyImageLabel.setObjectName("rightObliqueViewAnomalyImageLabel")
        self.gridLayout_2.addWidget(self.rightObliqueViewAnomalyImageLabel, 13, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 5, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.asymmetryImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asymmetryImageLabel.sizePolicy().hasHeightForWidth())
        self.asymmetryImageLabel.setSizePolicy(sizePolicy)
        self.asymmetryImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.asymmetryImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.asymmetryImageLabel.setText("")
        self.asymmetryImageLabel.setObjectName("asymmetryImageLabel")
        self.gridLayout_2.addWidget(self.asymmetryImageLabel, 1, 2, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 10, 2, 1, 1)
        self.rightLateralViewAnomalyImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightLateralViewAnomalyImageLabel.sizePolicy().hasHeightForWidth())
        self.rightLateralViewAnomalyImageLabel.setSizePolicy(sizePolicy)
        self.rightLateralViewAnomalyImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.rightLateralViewAnomalyImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.rightLateralViewAnomalyImageLabel.setText("")
        self.rightLateralViewAnomalyImageLabel.setObjectName("rightLateralViewAnomalyImageLabel")
        self.gridLayout_2.addWidget(self.rightLateralViewAnomalyImageLabel, 7, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem7, 11, 2, 1, 1)
        self.frontViewAnomalyImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontViewAnomalyImageLabel.sizePolicy().hasHeightForWidth())
        self.frontViewAnomalyImageLabel.setSizePolicy(sizePolicy)
        self.frontViewAnomalyImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.frontViewAnomalyImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frontViewAnomalyImageLabel.setText("")
        self.frontViewAnomalyImageLabel.setObjectName("frontViewAnomalyImageLabel")
        self.gridLayout_2.addWidget(self.frontViewAnomalyImageLabel, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem8, 11, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.backButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.backButton.setObjectName("backButton")
        self.gridLayout_2.addWidget(self.backButton, 17, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.leftLateralViewAnomalyImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftLateralViewAnomalyImageLabel.sizePolicy().hasHeightForWidth())
        self.leftLateralViewAnomalyImageLabel.setSizePolicy(sizePolicy)
        self.leftLateralViewAnomalyImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.leftLateralViewAnomalyImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.leftLateralViewAnomalyImageLabel.setText("")
        self.leftLateralViewAnomalyImageLabel.setObjectName("leftLateralViewAnomalyImageLabel")
        self.gridLayout_2.addWidget(self.leftLateralViewAnomalyImageLabel, 7, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 12, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.nextButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_2.addWidget(self.nextButton, 17, 2, 1, 1, QtCore.Qt.AlignRight)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem9, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem10, 16, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        anomalyDetectionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(anomalyDetectionWindow)
        self.statusbar.setObjectName("statusbar")
        anomalyDetectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(anomalyDetectionWindow)
        QtCore.QMetaObject.connectSlotsByName(anomalyDetectionWindow)

        self.window = anomalyDetectionWindow
        self.setupWidgets()
        self.progress = 0
        self.updateImageLabels()

    def retranslateUi(self, anomalyDetectionWindow):
        _translate = QtCore.QCoreApplication.translate
        anomalyDetectionWindow.setWindowTitle(_translate("anomalyDetectionWindow", "Thermal Anomaly Screen"))
        self.label_7.setText(_translate("anomalyDetectionWindow", "Right Lateral View"))
        self.label_8.setText(_translate("anomalyDetectionWindow", "Left Lateral View"))
        self.label_4.setText(_translate("anomalyDetectionWindow", "Asymmetry"))
        self.label_11.setText(_translate("anomalyDetectionWindow", "Right Oblique View"))
        self.backButton.setText(_translate("anomalyDetectionWindow", "Back"))
        self.label_12.setText(_translate("anomalyDetectionWindow", "Left Oblique View"))
        self.nextButton.setText(_translate("anomalyDetectionWindow", "Proceed to Next Window"))
        self.label_3.setText(_translate("anomalyDetectionWindow", "Frontal View"))

    def setupWidgets(self):
        self.backButton.clicked.connect(lambda:self.buttonClicked(self.backButton))
        self.nextButton.clicked.connect(lambda:self.buttonClicked(self.nextButton))

    def buttonClicked(self, button):
        if button == self.backButton:
            self.window.close()
            window = self.window
            cache = self.cache
            del self.window
            del self.cache
            ImageSelectionScreen.ImageSelectionScreen(window, cache)
            window.showMaximized()
        elif button == self.nextButton:
            self.window.close()
            window = self.window
            cache = self.cache
            del self.window
            del self.cache
            obj = EdgeDetectionScreen.EdgeDetectionScreen(window, cache)
            window.showMaximized()
            obj.preprocessScreen()

    def updateImageLabels(self):
        labels = [self.frontViewAnomalyImageLabel, self.rightLateralViewAnomalyImageLabel, self.leftLateralViewAnomalyImageLabel, self.rightObliqueViewAnomalyImageLabel, self.leftObliqueViewAnomalyImageLabel]
        for i in range(len(self.cache.anomalies)):
            if self.cache.anomalies[i] is not None:
                qimage = imageConversion(self.cache.anomalies[i])
                showOnWidget(labels[i], qimage)
                self.progress += 15
                self.progressBar.setValue(self.progress)
                
        if self.cache.asymmetryImage is not None:
            qimage = imageConversion(self.cache.asymmetryImage)
            showOnWidget(self.asymmetryImageLabel, qimage)
            self.progress += 25
            self.progressBar.setValue(self.progress)

    def updateAnomalyImageLabel(self, idx):
        labels = [self.frontViewAnomalyImageLabel, self.rightLateralViewAnomalyImageLabel, self.leftLateralViewAnomalyImageLabel, self.rightObliqueViewAnomalyImageLabel, self.leftObliqueViewAnomalyImageLabel]
        qimage = imageConversion(self.cache.anomalies[idx])
        showOnWidget(labels[idx], qimage)
        self.progress += 15
        self.progressBar.setValue(self.progress)

    def updateAsymmetryImageLabel(self):
        qimage = imageConversion(self.cache.asymmetryImage)
        showOnWidget(self.asymmetryImageLabel, qimage)
        self.progress += 25
        self.progressBar.setValue(self.progress)

    def stallScreen(self):
        self.progressBar.setEnabled(True)
        self.deactivateButtons()

    def restoreScreen(self):
        del self.master
        self.progressBar.setEnabled(False)
        self.activateButtons()

    def preprocessScreen(self):
        self.stallScreen()
        self.master = MasterThread(self.cache, self)
        self.master.createThreads()
        ret = self.master.startThreads()
        if ret is False:
            self.restoreScreen()

    def deactivateButtons(self):
        self.backButton.setEnabled(False)
        self.nextButton.setEnabled(False)

    def activateButtons(self):
        self.backButton.setEnabled(True)
        self.nextButton.setEnabled(True)
        

from PyQt5.QtCore import QThread, QObject, QMutex, pyqtSignal, pyqtSlot
import cv2 as cv
import numpy as np
from AnomalyDetection import AnomalyDetection

class MasterThread:
    def __init__(self, cache, screen):
        self.cache = cache
        self.screen = screen
        self.objs = list()
        self.threads = list()
        self.mutex = QMutex()

    def createThreads(self):
        for i in range(len(self.cache.anomalies)):
            if self.cache.anomalies[i] is None:
                obj = AnomalyWorkerThread(i, self.cache.roiMasks[i], self.cache.originalImages[i], self.cache.normalBodyColorPos, self.mutex)
                thread = QThread()
                obj.sendResult.connect(self.receiveAnomaly)
                obj.moveToThread(thread)
                obj.finished.connect(thread.quit)
                thread.started.connect(obj.doWork)
                thread.finished.connect(self.checkThreads)
                self.objs.append(obj)
                self.threads.append(thread)
            else:
                self.objs.append(None)
                self.threads.append(None)
        if self.cache.asymmetryImage is None:
            obj = AsymmetryWorkerThread(self.cache.rightMask, self.cache.leftMask, self.cache.originalImages[0], self.mutex)
            thread = QThread()
            obj.sendResult.connect(self.receiveAsymmetry)
            obj.moveToThread(thread)
            obj.finished.connect(thread.quit)
            thread.started.connect(obj.doWork)
            thread.finished.connect(self.checkThreads)
            self.objs.append(obj)
            self.threads.append(thread)
        else:
            self.objs.append(None)
            self.threads.append(None)

    def startThreads(self):
        ret = False
        for thread in self.threads:
            if thread is not None:
                ret = True
                thread.start()
        return ret
        
    def receiveAnomaly(self, idx, image):
        self.cache.anomalies[idx] = image
        self.screen.updateAnomalyImageLabel(idx)

    def receiveAsymmetry(self, image):
        self.cache.asymmetryImage = image
        self.screen.updateAsymmetryImageLabel()

    def checkThreads(self):
        boom = True
        for thread in self.threads:
            if thread is not None:
                if thread.isRunning() == True:
                    boom = False
                    break
        if boom == True:
            self.screen.restoreScreen()

    def __del__(self):
        for thread in self.threads:
            if thread is not None:
                thread.exit()
                thread.wait()
        self.threads.clear()
        self.objs.clear()
        del self.threads
        del self.objs
        del self.mutex
        del self.cache
        del self.screen

class AnomalyWorkerThread(QObject):
    finished = pyqtSignal()
    sendResult = pyqtSignal(int, np.ndarray)

    def __init__(self, idx, roi, original, normalBodyColorPos, mutex):
        super().__init__()
        self.idx = idx
        self.roi = roi
        self.original = original
        self.normalBodyColorPos = normalBodyColorPos
        self.mutex = mutex

    def doWork(self):
        # generate anomaly image using self.roi, self.original, self.normalBodyColorPos
        #'''
        anomaly = AnomalyDetection(self.original, self.roi)
        anomaly.find_anomaly()
        anomalyImage = anomaly.get_anomaly()
        #'''
        self.mutex.lock()
        self.sendResult.emit(self.idx, anomalyImage)
        self.finished.emit()
        self.mutex.unlock()

    def __del__(self):
        #super().__del__()
        #del self.finished
        #del self.sendResult
        del self.idx
        del self.roi
        del self.original
        del self.normalBodyColorPos
        del self.mutex

class AsymmetryWorkerThread(QObject):
    finished = pyqtSignal()
    sendResult = pyqtSignal(np.ndarray)

    def __init__(self, rightMask, leftMask, original, mutex):
        super().__init__()
        self.rightMask = rightMask
        self.leftMask = leftMask
        self.original = original
        self.mutex = mutex

    def doWork(self):
        # generate asymmetry image using self.rightMask, self.leftMask, self.original
        #'''
        asymmetryImage = self.original.copy()
        #'''
        self.mutex.lock()
        self.sendResult.emit(asymmetryImage)
        self.finished.emit()
        self.mutex.unlock()

    def __del__(self):
        #super().__del__()
        #del self.finished
        #del self.sendResult
        del self.rightMask
        del self.leftMask
        del self.original
        del self.mutex
        

##import sys
##from PyQt5.QtGui     import *
##from PyQt5.QtCore    import *
##from PyQt5.QtWidgets import *
##
##class Window(QMainWindow):
##    def __init__(self):
##        super().__init__()
##        self.title = "App"
##        self.top = 100
##        self.left = 100
##        self.width = 680
##        self.height = 500
##        self.InitUI()
##
##    def InitUI(self):
##        self.setWindowTitle(self.title)
##        self.setGeometry(self.top, self.left, self.width, self.height)
##
##        buttonWindow1 = QPushButton('Window1', self)
##        buttonWindow1.move(100, 100)
##        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
##        self.show()
##
##    def generateCache(self):
##        cache = Cache()
##        import cv2 as cv
##        for i in range(len(cache.originalImages)):
##            image = cv.imread("thermal_image.jpg")
##            image = cv.resize(image, (640, 480), interpolation = cv.INTER_LANCZOS4)
##            cache.originalImages[i] = image
##        for i in range(len(cache.roiMasks)):
##            image = cv.imread("roi.jpg")
##            image = cv.resize(image, (640, 480), interpolation = cv.INTER_LANCZOS4)
##            cache.roiMasks[i] = image
##        rightROI = cv.imread("rightROI.jpg")
##        rightROI = cv.resize(rightROI, (640, 480), interpolation = cv.INTER_LANCZOS4)
##        cache.rightMask = rightROI
##        leftROI = cv.imread("leftROI.jpg")
##        leftROI = cv.resize(leftROI, (640, 480), interpolation = cv.INTER_LANCZOS4)
##        cache.leftMask = leftROI
##        cache.normalBodyColor = [21, 188, 111]
##        cache.normalBodyColorPos = [345, 95] # [281,598] -> green;  [345, 95] -> yellow
##        temp = cv.imread("yellow.jpg")
##        temp = cv.resize(temp, (640, 480), interpolation = cv.INTER_LANCZOS4)
##        cache.anomalies[3] = temp
##        return cache
##
##    @pyqtSlot()
##    def buttonWindow1_onClick(self):
##        self.close()
##        cache = self.generateCache()
##        self.obj = AnomalyDetectionScreen(self, cache)
##        self.show()
##        self.obj.preprocessScreen()
##
##if __name__ == '__main__':
##    app=QApplication(sys.argv)
##    ex=Window()
##    sys.exit(app.exec_())
    
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    anomalyDetectionWindow = QtWidgets.QMainWindow()

    cache = Cache()
    import cv2 as cv
    for i in range(len(cache.originalImages)):
        image = cv.imread("thermal_image.jpg")
        image = cv.resize(image, (640, 480), interpolation = cv.INTER_LANCZOS4)
        cache.originalImages[i] = image
    for i in range(len(cache.roiMasks)):
        image = cv.imread("roi.jpg")
        image = cv.resize(image, (640, 480), interpolation = cv.INTER_LANCZOS4)
        cache.roiMasks[i] = image
    rightROI = cv.imread("rightROI.jpg")
    rightROI = cv.resize(rightROI, (640, 480), interpolation = cv.INTER_LANCZOS4)
    cache.rightMask = rightROI
    leftROI = cv.imread("leftROI.jpg")
    leftROI = cv.resize(leftROI, (640, 480), interpolation = cv.INTER_LANCZOS4)
    cache.leftMask = leftROI
    cache.normalBodyColor = [21, 188, 111]
    cache.normalBodyColorPos = [345, 95] # [281,598] -> green;  [345, 95] -> yellow
    
    ui = AnomalyDetectionScreen(anomalyDetectionWindow, cache)
    anomalyDetectionWindow.show()
    sys.exit(app.exec_())
'''
