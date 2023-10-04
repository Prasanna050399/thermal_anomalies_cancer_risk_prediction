from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import numpy as np
import cv2 as cv
from Cache import Cache
from Image import imageConversion, showOnWidget
from PreProcessing import PreProcessing
import PatientDataScreen
import AnomalyDetectionScreen

class ImageSelectionScreen(object):
    def __init__(self, window, cache=None):
        window.__init__()
        self.cache = cache
        self.row = None
        self.column = None
        self.setupUi(window)
        #window.showMaximized() ## remove on integration
        
    def setupUi(self, imageSelectionWindow):
        imageSelectionWindow.setObjectName("imageSelectionWindow")
        imageSelectionWindow.resize(1200, 600)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.font = font
        imageSelectionWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(imageSelectionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1344, 1951))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_2.addWidget(self.nextButton, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        self.leftLateralViewGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.leftLateralViewGroupBox.setObjectName("leftLateralViewGroupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.leftLateralViewGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.leftLateralViewImageLabel = QtWidgets.QLabel(self.leftLateralViewGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftLateralViewImageLabel.sizePolicy().hasHeightForWidth())
        self.leftLateralViewImageLabel.setSizePolicy(sizePolicy)
        self.leftLateralViewImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.leftLateralViewImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.leftLateralViewImageLabel.setText("")
        self.leftLateralViewImageLabel.setObjectName("leftLateralViewImageLabel")
        self.gridLayout_6.addWidget(self.leftLateralViewImageLabel, 0, 0, 1, 1)
        self.importLeftLateralViewImageButton = QtWidgets.QPushButton(self.leftLateralViewGroupBox)
        self.importLeftLateralViewImageButton.setObjectName("importLeftLateralViewImageButton")
        self.gridLayout_6.addWidget(self.importLeftLateralViewImageButton, 1, 0, 1, 1)
        self.leftLateralViewRoiButton = QtWidgets.QPushButton(self.leftLateralViewGroupBox)
        self.leftLateralViewRoiButton.setObjectName("leftLateralViewRoiButton")
        self.gridLayout_6.addWidget(self.leftLateralViewRoiButton, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.leftLateralViewGroupBox, 1, 1, 1, 1)
        self.rightObliqueViewGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.rightObliqueViewGroupBox.setObjectName("rightObliqueViewGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.rightObliqueViewGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.rightObliqueViewImageLabel = QtWidgets.QLabel(self.rightObliqueViewGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightObliqueViewImageLabel.sizePolicy().hasHeightForWidth())
        self.rightObliqueViewImageLabel.setSizePolicy(sizePolicy)
        self.rightObliqueViewImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.rightObliqueViewImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.rightObliqueViewImageLabel.setText("")
        self.rightObliqueViewImageLabel.setObjectName("rightObliqueViewImageLabel")
        self.gridLayout_5.addWidget(self.rightObliqueViewImageLabel, 0, 0, 1, 1)
        self.importRightObliqueViewImageButton = QtWidgets.QPushButton(self.rightObliqueViewGroupBox)
        self.importRightObliqueViewImageButton.setObjectName("importRightObliqueViewImageButton")
        self.gridLayout_5.addWidget(self.importRightObliqueViewImageButton, 1, 0, 1, 1)
        self.rightObliqueViewRoiButton = QtWidgets.QPushButton(self.rightObliqueViewGroupBox)
        self.rightObliqueViewRoiButton.setObjectName("rightObliqueViewRoiButton")
        self.gridLayout_5.addWidget(self.rightObliqueViewRoiButton, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.rightObliqueViewGroupBox, 2, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setObjectName("backButton")
        self.gridLayout_2.addWidget(self.backButton, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.rightLateralViewGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.rightLateralViewGroupBox.setObjectName("rightLateralViewGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.rightLateralViewGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.importRightLateralViewImageButton = QtWidgets.QPushButton(self.rightLateralViewGroupBox)
        self.importRightLateralViewImageButton.setObjectName("importRightLateralViewImageButton")
        self.gridLayout_4.addWidget(self.importRightLateralViewImageButton, 1, 0, 1, 1)
        self.rightLateralViewImageLabel = QtWidgets.QLabel(self.rightLateralViewGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightLateralViewImageLabel.sizePolicy().hasHeightForWidth())
        self.rightLateralViewImageLabel.setSizePolicy(sizePolicy)
        self.rightLateralViewImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.rightLateralViewImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.rightLateralViewImageLabel.setText("")
        self.rightLateralViewImageLabel.setObjectName("rightLateralViewImageLabel")
        self.gridLayout_4.addWidget(self.rightLateralViewImageLabel, 0, 0, 1, 1)
        self.rightLateralViewRoiButton = QtWidgets.QPushButton(self.rightLateralViewGroupBox)
        self.rightLateralViewRoiButton.setObjectName("rightLateralViewRoiButton")
        self.gridLayout_4.addWidget(self.rightLateralViewRoiButton, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.rightLateralViewGroupBox, 1, 0, 1, 1)
        self.frontalViewGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.frontalViewGroupBox.setObjectName("frontalViewGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frontalViewGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frontViewLeftRoiButton = QtWidgets.QPushButton(self.frontalViewGroupBox)
        self.frontViewLeftRoiButton.setObjectName("frontViewLeftRoiButton")
        self.gridLayout_3.addWidget(self.frontViewLeftRoiButton, 6, 0, 1, 1)
        self.selectNormalTemperaturePointButton = QtWidgets.QPushButton(self.frontalViewGroupBox)
        self.selectNormalTemperaturePointButton.setObjectName("selectNormalTemperaturePointButton")
        self.gridLayout_3.addWidget(self.selectNormalTemperaturePointButton, 7, 0, 1, 1)
        self.frontalViewImageLabel = QtWidgets.QLabel(self.frontalViewGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontalViewImageLabel.sizePolicy().hasHeightForWidth())
        self.frontalViewImageLabel.setSizePolicy(sizePolicy)
        self.frontalViewImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.frontalViewImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frontalViewImageLabel.setText("")
        self.frontalViewImageLabel.setObjectName("frontalViewImageLabel")
        self.gridLayout_3.addWidget(self.frontalViewImageLabel, 0, 0, 4, 1)
        self.importFrontViewImageButton = QtWidgets.QPushButton(self.frontalViewGroupBox)
        self.importFrontViewImageButton.setObjectName("importFrontViewImageButton")
        self.gridLayout_3.addWidget(self.importFrontViewImageButton, 4, 0, 1, 1)
        self.frontViewRightRoiButton = QtWidgets.QPushButton(self.frontalViewGroupBox)
        self.frontViewRightRoiButton.setObjectName("frontViewRightRoiButton")
        self.gridLayout_3.addWidget(self.frontViewRightRoiButton, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frontalViewGroupBox, 0, 0, 1, 2)
        self.leftObliqueViewGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.leftObliqueViewGroupBox.setObjectName("leftObliqueViewGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.leftObliqueViewGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.leftObliqueViewImageLabel = QtWidgets.QLabel(self.leftObliqueViewGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftObliqueViewImageLabel.sizePolicy().hasHeightForWidth())
        self.leftObliqueViewImageLabel.setSizePolicy(sizePolicy)
        self.leftObliqueViewImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.leftObliqueViewImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.leftObliqueViewImageLabel.setText("")
        self.leftObliqueViewImageLabel.setObjectName("leftObliqueViewImageLabel")
        self.gridLayout_7.addWidget(self.leftObliqueViewImageLabel, 0, 0, 1, 1)
        self.importLeftObliqueViewImageButton = QtWidgets.QPushButton(self.leftObliqueViewGroupBox)
        self.importLeftObliqueViewImageButton.setObjectName("importLeftObliqueViewImageButton")
        self.gridLayout_7.addWidget(self.importLeftObliqueViewImageButton, 1, 0, 1, 1)
        self.leftObliqueViewRoiButton = QtWidgets.QPushButton(self.leftObliqueViewGroupBox)
        self.leftObliqueViewRoiButton.setObjectName("leftObliqueViewRoiButton")
        self.gridLayout_7.addWidget(self.leftObliqueViewRoiButton, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.leftObliqueViewGroupBox, 2, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        imageSelectionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(imageSelectionWindow)
        self.statusbar.setObjectName("statusbar")
        imageSelectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(imageSelectionWindow)
        QtCore.QMetaObject.connectSlotsByName(imageSelectionWindow)
        
        self.window = imageSelectionWindow
        self.updateImageLabels()
        self.setupWidgets()
    
    def retranslateUi(self, imageSelectionWindow):
        _translate = QtCore.QCoreApplication.translate
        imageSelectionWindow.setWindowTitle(_translate("imageSelectionWindow", "Import Images Screen"))
        self.nextButton.setText(_translate("imageSelectionWindow", "Proceed to Next Window"))
        self.leftLateralViewGroupBox.setTitle(_translate("imageSelectionWindow", "Left Lateral View"))
        self.importLeftLateralViewImageButton.setText(_translate("imageSelectionWindow", "Import Image"))
        self.leftLateralViewRoiButton.setText(_translate("imageSelectionWindow", "Select ROI"))
        self.rightObliqueViewGroupBox.setTitle(_translate("imageSelectionWindow", "Right Oblique View"))
        self.importRightObliqueViewImageButton.setText(_translate("imageSelectionWindow", "Import Image"))
        self.rightObliqueViewRoiButton.setText(_translate("imageSelectionWindow", "Select ROI"))
        self.backButton.setText(_translate("imageSelectionWindow", "Back"))
        self.rightLateralViewGroupBox.setTitle(_translate("imageSelectionWindow", "Right Lateral View"))
        self.importRightLateralViewImageButton.setText(_translate("imageSelectionWindow", "Import Image"))
        self.rightLateralViewRoiButton.setText(_translate("imageSelectionWindow", "Select ROI"))
        self.frontalViewGroupBox.setTitle(_translate("imageSelectionWindow", "Frontal View"))
        self.frontViewLeftRoiButton.setText(_translate("imageSelectionWindow", "Select Left ROI"))
        self.selectNormalTemperaturePointButton.setText(_translate("imageSelectionWindow", "Select Normal Temperature Point"))
        self.importFrontViewImageButton.setText(_translate("imageSelectionWindow", "Import Image"))
        self.frontViewRightRoiButton.setText(_translate("imageSelectionWindow", "Select Right ROI"))
        self.leftObliqueViewGroupBox.setTitle(_translate("imageSelectionWindow", "Left Oblique View"))
        self.importLeftObliqueViewImageButton.setText(_translate("imageSelectionWindow", "Import Image"))
        self.leftObliqueViewRoiButton.setText(_translate("imageSelectionWindow", "Select ROI"))

    def setupWidgets(self):
        self.backButton.clicked.connect(lambda:self.buttonClicked(self.backButton))
        self.nextButton.clicked.connect(lambda:self.buttonClicked(self.nextButton))
        
        # image import buttons
        self.importFrontViewImageButton.clicked.connect(lambda:self.openImageFromSystem(0))
        self.importRightLateralViewImageButton.clicked.connect(lambda:self.openImageFromSystem(1))
        self.importLeftLateralViewImageButton.clicked.connect(lambda:self.openImageFromSystem(2))
        self.importRightObliqueViewImageButton.clicked.connect(lambda:self.openImageFromSystem(3))
        self.importLeftObliqueViewImageButton.clicked.connect(lambda:self.openImageFromSystem(4))

        # roi selection buttons
        self.frontViewRightRoiButton.clicked.connect(lambda:self.selectROI(0, side = "right"))
        self.frontViewLeftRoiButton.clicked.connect(lambda:self.selectROI(0, side = "left"))
        self.rightLateralViewRoiButton.clicked.connect(lambda:self.selectROI(1))
        self.leftLateralViewRoiButton.clicked.connect(lambda:self.selectROI(2))
        self.rightObliqueViewRoiButton.clicked.connect(lambda:self.selectROI(3))
        self.leftObliqueViewRoiButton.clicked.connect(lambda:self.selectROI(4))

        # select normal temperature point button
        self.selectNormalTemperaturePointButton.clicked.connect(self.selectNormalTemperaturePoint)

    def buttonClicked(self, button):
        if button == self.backButton:
            self.window.close()
            window = self.window
            cache = self.cache
            del self.window
            #del self.cache
            PatientDataScreen.PatientDataScreen(window, cache)
            window.showMaximized()
        elif button == self.nextButton:
            if self.nextButtonCheck() is True:
                print("leave")
                self.window.close()
                window = self.window
                cache = self.cache
                del self.window
                del self.cache
                obj = AnomalyDetectionScreen.AnomalyDetectionScreen(window, cache)
                window.showMaximized()
                obj.preprocessScreen()
            else:
                print("stay")
                failureMsgBox = QMessageBox()
                failureMsgBox.setIcon(QMessageBox.Warning)
                failureMsgBox.setWindowTitle("Insufficient Resources to proceed")
                failureMsgBox.setText("One or more entities required to proceed are not Available.")
                additionalText = "Following entities are not available, please select them before proceeding:"
                entities = self.findEntitiesNotAvailable()
                num = 1
                for entity in entities:
                    additionalText = additionalText + "\n\t" + str(num) + "] " + entity
                    num += 1
                failureMsgBox.setInformativeText(additionalText)
                failureMsgBox.setStandardButtons(QMessageBox.Ok)
                failureMsgBox.exec_()

    def findEntitiesNotAvailable(self):
        res = []
        entities = [["Front view scan image", "Front view Right ROI", "Front view Left ROI", "Normal Temperature point"], ["Right lateral view scan image", "Right lateral view ROI"], ["Left lateral view scan image", "Left lateral view ROI"], ["Right oblique view scan image", "Right oblique view ROI"], ["Left oblique view scan image", "Left oblique view ROI"]]
        for i in range(len(entities)):
            if i == 0:
                if self.cache.originalImages[i] is None:
                    res.append(entities[i][0])
                if self.cache.rightMask is None:
                    res.append(entities[i][1])
                if self.cache.leftMask is None:
                    res.append(entities[i][2])
                if self.cache.normalBodyColor[0] is None or self.cache.normalBodyColor[1] is None or self.cache.normalBodyColor[2] is None or self.cache.normalBodyColorPos[0] is None or self.cache.normalBodyColorPos[1] is None or self.cache.normalBodyColorGray is None:
                    res.append(entities[i][3])
            else:
                if self.cache.originalImages[i] is None:
                    res.append(entities[i][0])
                if self.cache.roiMasks[i] is None:
                    res.append(entities[i][1])
        return res

    def blockButtons(self):
        self.backButton.setEnabled(False)
        self.nextButton.setEnabled(False)

    def unblockButtons(self):
        self.backButton.setEnabled(True)
        self.nextButton.setEnabled(True)

    def blockIdx(self, idx):
        self.blockButtons()
        buttons = [[self.importFrontViewImageButton, self.frontViewRightRoiButton, self.frontViewLeftRoiButton, self.selectNormalTemperaturePointButton], [self.importRightLateralViewImageButton, self.rightLateralViewRoiButton], [self.importLeftLateralViewImageButton, self.leftLateralViewRoiButton], [self.importRightObliqueViewImageButton, self.rightObliqueViewRoiButton], [self.importLeftObliqueViewImageButton, self.leftObliqueViewRoiButton]]
        for button in buttons[idx]:
            button.setEnabled(False)
        for i in range(len(buttons)):
            if i == idx:
                continue
            else:
                for button in buttons[i]:
                    button.setEnabled(True)

    def unblockIdx(self, idx):
        self.unblockButtons()
        buttons = [[self.importFrontViewImageButton, self.frontViewRightRoiButton, self.frontViewLeftRoiButton, self.selectNormalTemperaturePointButton], [self.importRightLateralViewImageButton, self.rightLateralViewRoiButton], [self.importLeftLateralViewImageButton, self.leftLateralViewRoiButton], [self.importRightObliqueViewImageButton, self.rightObliqueViewRoiButton], [self.importLeftObliqueViewImageButton, self.leftObliqueViewRoiButton]]
        for button in buttons[idx]:
            button.setEnabled(True)

    def blockAll(self):
        self.blockButtons()
        buttons = [[self.importFrontViewImageButton, self.frontViewRightRoiButton, self.frontViewLeftRoiButton, self.selectNormalTemperaturePointButton], [self.importRightLateralViewImageButton, self.rightLateralViewRoiButton], [self.importLeftLateralViewImageButton, self.leftLateralViewRoiButton], [self.importRightObliqueViewImageButton, self.rightObliqueViewRoiButton], [self.importLeftObliqueViewImageButton, self.leftObliqueViewRoiButton]]
        for i in range(len(buttons)):
            for button in buttons[i]:
                button.setEnabled(False)

    def unblockAll(self):
        self.unblockButtons()
        buttons = [[self.importFrontViewImageButton, self.frontViewRightRoiButton, self.frontViewLeftRoiButton, self.selectNormalTemperaturePointButton], [self.importRightLateralViewImageButton, self.rightLateralViewRoiButton], [self.importLeftLateralViewImageButton, self.leftLateralViewRoiButton], [self.importRightObliqueViewImageButton, self.rightObliqueViewRoiButton], [self.importLeftObliqueViewImageButton, self.leftObliqueViewRoiButton]]
        for i in range(len(buttons)):
            for button in buttons[i]:
                button.setEnabled(True)

    def openImageFromSystem(self, idx):
        filename = self.openFileNameDialog()
        print(filename) ##
        image = cv.imread(filename)
        if image is None:
            self.throwInvalidImageError()
        else:
            image = self.preprocessImage(image)
            self.cache.originalImages[idx] = image
            if idx == 0:
                self.cache.rightMask = None
                self.cache.leftMask = None
                self.cache.roiMasks[0] = None
                #self.cache.asymmetryImage = None ##
                self.cache.normalBodyColor = [None, None, None]
                self.cache.normalBodyColorPos = [None, None]
                self.cache.normalBodyColorGray = None
                self.importFrontViewImageButton.setStyleSheet('background-color:gray')
                self.importFrontViewImageButton.setFont(self.font)
                self.frontViewRightRoiButton.setStyleSheet('')
                self.frontViewRightRoiButton.setFont(self.font)
                self.frontViewLeftRoiButton.setStyleSheet('')
                self.frontViewLeftRoiButton.setFont(self.font)
                self.selectNormalTemperaturePointButton.setStyleSheet('')
                self.selectNormalTemperaturePointButton.setFont(self.font)
                self.clearUnnecessaryCache()
            else:
                self.cache.roiMasks[idx] = None
                buttons = [[self.importFrontViewImageButton, self.frontViewRightRoiButton, self.frontViewLeftRoiButton, self.selectNormalTemperaturePointButton], [self.importRightLateralViewImageButton, self.rightLateralViewRoiButton], [self.importLeftLateralViewImageButton, self.leftLateralViewRoiButton], [self.importRightObliqueViewImageButton, self.rightObliqueViewRoiButton], [self.importLeftObliqueViewImageButton, self.leftObliqueViewRoiButton]]
                buttons[idx][0].setStyleSheet('background-color:gray')
                buttons[idx][0].setFont(self.font)
                buttons[idx][1].setStyleSheet('')
                buttons[idx][1].setFont(self.font)
            self.clearUnnecessaryCache(idx)
            self.cache.print() ##
            self.updateImageLabels()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.window, "QFileDialog.getOpenFileName()", "","All Files (*);;JPG Files (*.jpg);;PNG Files (*.png)", options=options)
        return fileName

    def preprocessImage(self, image):
        image = cv.resize(image, (640, 480), interpolation = cv.INTER_LANCZOS4)
        return image

    def selectROI(self, idx, side = None):
        if self.cache.originalImages[idx] is None:
            self.throwImageNotSelectedError()
            return
        self.roiSelectionPopup()
        self.blockIdx(idx)
        obj = PreProcessing()
        res = obj.get_ROI(self.cache.originalImages[idx])
        if res is None:
            self.unblockIdx(idx)
            return
        if idx == 0:
            if side == "right":
                self.cache.rightMask = res
                #self.cache.asymmetryImage = None ##
                self.frontViewRightRoiButton.setStyleSheet('background-color:gray')
                self.frontViewRightRoiButton.setFont(self.font)
            elif side == "left":
                self.cache.leftMask = res
                #self.cache.asymmetryImage = None ##
                self.frontViewLeftRoiButton.setStyleSheet('background-color:gray')
                self.frontViewLeftRoiButton.setFont(self.font)
            temp = self.calculateFrontROIMask()
            if temp is not None:
                res = self.calculateROI(0)
                self.cache.roiMasks[0] = res
                cv.imshow("Selected ROI", res)
                cv.waitKey()
            else:
                res = self.calculateROI(0)
                cv.imshow("Selected ROI", res)
                cv.waitKey()
        else:
            buttons = [[self.importFrontViewImageButton, self.frontViewRightRoiButton, self.frontViewLeftRoiButton, self.selectNormalTemperaturePointButton], [self.importRightLateralViewImageButton, self.rightLateralViewRoiButton], [self.importLeftLateralViewImageButton, self.leftLateralViewRoiButton], [self.importRightObliqueViewImageButton, self.rightObliqueViewRoiButton], [self.importLeftObliqueViewImageButton, self.leftObliqueViewRoiButton]]
            self.cache.roiMasks[idx] = res
            res = self.calculateROI(idx)
            self.cache.roiMasks[idx] = res
            buttons[idx][1].setStyleSheet('background-color:gray')
            buttons[idx][1].setFont(self.font)
            cv.imshow("Selected ROI", res)
            cv.waitKey()
        self.clearUnnecessaryCache(idx)
        self.unblockIdx(idx)
        self.cache.print() ##

    def calculateFrontROIMask(self):
        if self.cache.rightMask is not None and self.cache.leftMask is not None:
            res = cv.bitwise_or(self.cache.rightMask, self.cache.leftMask)
            self.cache.roiMasks[0] = res
            return res
        return None

    def calculateROI(self, idx):
        if idx == 0:
            if self.cache.roiMasks[0] is None:
                if self.cache.rightMask is not None:
                    curImage = self.cache.originalImages[0]
                    maskImage = self.cache.rightMask
                    maskImage = cv.cvtColor(maskImage, cv.COLOR_GRAY2BGR)
                    roi = cv.bitwise_and(curImage, maskImage)
                    return roi
                elif self.cache.leftMask is not None:
                    curImage = self.cache.originalImages[0]
                    maskImage = self.cache.leftMask
                    maskImage = cv.cvtColor(maskImage, cv.COLOR_GRAY2BGR)
                    roi = cv.bitwise_and(curImage, maskImage)
                    return roi
        curImage = self.cache.originalImages[idx]
        maskImage = self.cache.roiMasks[idx]
        maskImage = cv.cvtColor(maskImage, cv.COLOR_GRAY2BGR)
        roi = cv.bitwise_and(curImage, maskImage)
        return roi

    def selectNormalTemperaturePoint(self):
        if self.cache.originalImages[0] is None:
            self.throwImageNotSelectedError()
            return
        self.blockIdx(0)
        image = self.cache.originalImages[0].copy()
        cv.imshow("Select Normal temperature point", image)
        cv.setMouseCallback('Select Normal temperature point', self.click_event)
        cv.waitKey()
        if self.row is None and self.column is None:
            self.unblockIdx(0)
            return
        self.cache.normalBodyColor[0] = image[self.row][self.column][0]
        self.cache.normalBodyColor[1] = image[self.row][self.column][1]
        self.cache.normalBodyColor[2] = image[self.row][self.column][2]
        self.cache.normalBodyColorPos[0] = self.row
        self.cache.normalBodyColorPos[1] = self.column
        self.saveGrayLevelOfNormalPointToCache()
        image = cv.circle(image, (self.column,self.row), 3, (255, 255, 255), 2)
        cv.imshow("Showing selected Normal temperature point", image)
        cv.waitKey()
        self.clearUnnecessaryCache(6)
        self.unblockIdx(0)
        self.selectNormalTemperaturePointButton.setStyleSheet('background-color:gray')
        self.selectNormalTemperaturePointButton.setFont(self.font)
        self.cache.print() ##

    def saveGrayLevelOfNormalPointToCache(self):
        image = self.cache.originalImages[0].copy();
        
        #'''
        # new method with image enhance and k-means
        enhance = cv.detailEnhance(image, sigma_s=10, sigma_r=0.15)
        img = cv.cvtColor(enhance, cv.COLOR_BGR2RGB)
        Z = img.reshape((-1,3))
        Z = np.float32(Z)
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 8
        ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))
        res2 = cv.cvtColor(res2, cv.COLOR_RGB2BGR)
        #gray = cv.cvtColor(res2, cv.COLOR_BGR2GRAY)
        coefficients = [0.1,0.6,0.1]
        m = np.array(coefficients).reshape((1,3))
        gray = cv.transform(res2, m)
        #'''
        
        '''
        # old method without image enhance and k-means
        #coefficients = [0.1,0.6,0.1]
        #m = np.array(coefficients).reshape((1,3))
        #gray = cv.transform(image, m)
        '''
        
        x, y = self.cache.normalBodyColorPos
        avg = 0
        count = 0
        for i in range(x-1,x+2):
            if i >= 480 or i < 0:
                continue
            for j in range(y-1,y+2):
                if j >= 640 or j < 0:
                    continue
                else:
                    avg += gray[i][j]
                    count += 1
        avg /= count
        self.cache.normalBodyColorGray = round(avg)
        
    def click_event(self, event, x, y, flags, params):
        if event == cv.EVENT_LBUTTONDOWN:
            print("Co-ordinates selected:", y, x) ##
            self.column = x
            self.row = y
            cv.destroyAllWindows()

    def updateImageLabels(self):
        self.blockAll()
        if self.cache.originalImages[0] is not None:
            qimage = imageConversion(self.cache.originalImages[0])
            showOnWidget(self.frontalViewImageLabel, qimage)
        if self.cache.originalImages[1] is not None:
            qimage = imageConversion(self.cache.originalImages[1])
            showOnWidget(self.rightLateralViewImageLabel, qimage)
        if self.cache.originalImages[2] is not None:
            qimage = imageConversion(self.cache.originalImages[2])
            showOnWidget(self.leftLateralViewImageLabel, qimage)
        if self.cache.originalImages[3] is not None:
            qimage = imageConversion(self.cache.originalImages[3])
            showOnWidget(self.rightObliqueViewImageLabel, qimage)
        if self.cache.originalImages[4] is not None:
            qimage = imageConversion(self.cache.originalImages[4])
            showOnWidget(self.leftObliqueViewImageLabel, qimage)
        buttons = [[self.importFrontViewImageButton, self.frontViewRightRoiButton, self.frontViewLeftRoiButton, self.selectNormalTemperaturePointButton], [self.importRightLateralViewImageButton, self.rightLateralViewRoiButton], [self.importLeftLateralViewImageButton, self.leftLateralViewRoiButton], [self.importRightObliqueViewImageButton, self.rightObliqueViewRoiButton], [self.importLeftObliqueViewImageButton, self.leftObliqueViewRoiButton]]
        for i in range(len(buttons)):
            if self.cache.originalImages[i] is not None:
                buttons[i][0].setStyleSheet('background-color:gray')
                buttons[i][0].setFont(self.font)
                if i == 0:
                    if self.cache.rightMask is not None:
                        self.frontViewRightRoiButton.setStyleSheet('background-color:gray')
                        self.frontViewRightRoiButton.setFont(self.font)
                    if self.cache.leftMask is not None:
                        self.frontViewLeftRoiButton.setStyleSheet('background-color:gray')
                        self.frontViewLeftRoiButton.setFont(self.font)
                    if self.cache.normalBodyColor[0] is not None and self.cache.normalBodyColor[1] is not None and self.cache.normalBodyColor[2] is not None:
                        self.selectNormalTemperaturePointButton.setStyleSheet('background-color:gray')
                        self.selectNormalTemperaturePointButton.setFont(self.font)
                else:
                    if self.cache.roiMasks[i] is not None:
                        buttons[i][1].setStyleSheet('background-color:gray')
                        buttons[i][1].setFont(self.font)
        self.unblockAll()

    def clearUnnecessaryCache(self, idx = 6):
        if idx == 6:
            for i in range(len(self.cache.anomalies)):
                self.cache.anomalies[i] = None
        else:
            self.cache.anomalies[idx] = None
            self.cache.edges[idx] = [None,0,255]

    def nextButtonCheck(self):
        return True ##
        for image in self.cache.originalImages:
            if image is None:
                return False
        if self.cache.rightMask is None:
            return False
        if self.cache.leftMask is None:
            return False
        if self.cache.normalBodyColor[0] is None or self.cache.normalBodyColor[1] is None or self.cache.normalBodyColor[2] is None or self.cache.normalBodyColorPos[0] is None or self.cache.normalBodyColorPos[1] is None or self.cache.normalBodyColorGray is None:
            return False
        for roi in self.cache.roiMasks:
            if roi is None:
                return False
        return True

    def throwInvalidImageError(self):
        failureMsgBox = QMessageBox()
        failureMsgBox.setIcon(QMessageBox.Critical)
        failureMsgBox.setWindowTitle("Invalid image Error")
        failureMsgBox.setText("Scan image import failed.")
        additionalText = "Image or file selected is not accessible or given file format is not a supported image file format."
        failureMsgBox.setInformativeText(additionalText)
        failureMsgBox.setStandardButtons(QMessageBox.Ok)
        failureMsgBox.exec_()

    def throwImageNotSelectedError(self):
        failureMsgBox = QMessageBox()
        failureMsgBox.setIcon(QMessageBox.Critical)
        failureMsgBox.setWindowTitle("Scan image not available Error")
        failureMsgBox.setText("Scan image for current slot is empty.")
        additionalText = "Please import scan image for current slot first."
        failureMsgBox.setInformativeText(additionalText)
        failureMsgBox.setStandardButtons(QMessageBox.Ok)
        failureMsgBox.exec_()

    def roiSelectionPopup(self):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setWindowTitle("Proceeding to ROI selection screen")
        infoBox.setText("Press OK button to continue")
        additionalText = "Press 'show details' button to see help for ROI screen."
        infoBox.setInformativeText(additionalText)
        infoBox.setDetailedText("Left Mouse Button : Plot ROI point at selected point.\nRight Mouse button : Remove last selected ROI point.\nEnter : Finalize selected ROI points.")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()


##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    imageSelectionWindow = QtWidgets.QMainWindow()
##
##    cache = Cache()
##    temp = cv.imread("thermal_image.jpg")
##    temp = cv.resize(temp, (640, 480), interpolation = cv.INTER_LANCZOS4)
##    cache.originalImages[0] = temp
##    temp = cv.imread("leftROI.jpg")
##    temp = cv.resize(temp, (640, 480), interpolation = cv.INTER_LANCZOS4)
##    temp = cv.cvtColor(temp, cv.COLOR_BGR2GRAY)
##    cache.leftMask = temp
##    temp = cv.imread("yellow.jpg")
##    temp = cv.resize(temp, (640, 480), interpolation = cv.INTER_LANCZOS4)
##    cache.originalImages[3] = temp
##    ui = ImageSelectionScreen(imageSelectionWindow, cache)
##    
##    #ui.setupUi(imageSelectionWindow)
##    imageSelectionWindow.showMaximized()
##    sys.exit(app.exec_())
