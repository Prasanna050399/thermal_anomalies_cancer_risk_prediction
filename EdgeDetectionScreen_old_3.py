from PyQt5 import QtCore, QtGui, QtWidgets
from Cache import Cache
from Image import imageConversion, showOnWidget
import AnomalyDetectionScreen
import RemarksScreen

class EdgeDetectionScreen(object):
    def __init__(self, window, cache=None):
        window.__init__()
        self.cache = cache
        self.setupUi(window)
        #window.showMaximized() ## remove on integration
        
    def setupUi(self, edgeDetectionWindow):
        edgeDetectionWindow.setObjectName("edgeDetectionWindow")
        edgeDetectionWindow.resize(1200, 600)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        edgeDetectionWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(edgeDetectionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1247, 1344, 2696))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 4, 0, 1, 2)
        self.nextButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_2.addWidget(self.nextButton, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 5, 0, 1, 1)
        self.rightLateralViewThreshApplyButton = QtWidgets.QPushButton(self.groupBox_2)
        self.rightLateralViewThreshApplyButton.setObjectName("rightLateralViewThreshApplyButton")
        self.gridLayout_4.addWidget(self.rightLateralViewThreshApplyButton, 10, 4, 1, 1)
        self.rightLateralViewEdgeAlgo = QtWidgets.QComboBox(self.groupBox_2)
        self.rightLateralViewEdgeAlgo.setObjectName("rightLateralViewEdgeAlgo")
        self.gridLayout_4.addWidget(self.rightLateralViewEdgeAlgo, 2, 0, 1, 6)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 7, 5, 1, 1, QtCore.Qt.AlignRight)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 7, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.rightLateralViewEdgeImageLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightLateralViewEdgeImageLabel.sizePolicy().hasHeightForWidth())
        self.rightLateralViewEdgeImageLabel.setSizePolicy(sizePolicy)
        self.rightLateralViewEdgeImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.rightLateralViewEdgeImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.rightLateralViewEdgeImageLabel.setText("")
        self.rightLateralViewEdgeImageLabel.setObjectName("rightLateralViewEdgeImageLabel")
        self.gridLayout_4.addWidget(self.rightLateralViewEdgeImageLabel, 0, 0, 1, 6, QtCore.Qt.AlignHCenter)
        self.rightLateralViewLowThreshField = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightLateralViewLowThreshField.sizePolicy().hasHeightForWidth())
        self.rightLateralViewLowThreshField.setSizePolicy(sizePolicy)
        self.rightLateralViewLowThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.rightLateralViewLowThreshField.setObjectName("rightLateralViewLowThreshField")
        self.gridLayout_4.addWidget(self.rightLateralViewLowThreshField, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 8, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 8, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 8, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem3, 12, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 4, 5, 1, 1, QtCore.Qt.AlignRight)
        self.rightLateralViewHighThreshField = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightLateralViewHighThreshField.sizePolicy().hasHeightForWidth())
        self.rightLateralViewHighThreshField.setSizePolicy(sizePolicy)
        self.rightLateralViewHighThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.rightLateralViewHighThreshField.setObjectName("rightLateralViewHighThreshField")
        self.gridLayout_4.addWidget(self.rightLateralViewHighThreshField, 8, 2, 1, 1)
        self.rightLateralViewHighThreshSlider = QtWidgets.QSlider(self.groupBox_2)
        self.rightLateralViewHighThreshSlider.setMaximum(255)
        self.rightLateralViewHighThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rightLateralViewHighThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rightLateralViewHighThreshSlider.setTickInterval(1)
        self.rightLateralViewHighThreshSlider.setObjectName("rightLateralViewHighThreshSlider")
        self.gridLayout_4.addWidget(self.rightLateralViewHighThreshSlider, 8, 4, 1, 2)
        self.rightLateralViewLowThreshSlider = QtWidgets.QSlider(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightLateralViewLowThreshSlider.sizePolicy().hasHeightForWidth())
        self.rightLateralViewLowThreshSlider.setSizePolicy(sizePolicy)
        self.rightLateralViewLowThreshSlider.setMaximum(255)
        self.rightLateralViewLowThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rightLateralViewLowThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rightLateralViewLowThreshSlider.setTickInterval(1)
        self.rightLateralViewLowThreshSlider.setObjectName("rightLateralViewLowThreshSlider")
        self.gridLayout_4.addWidget(self.rightLateralViewLowThreshSlider, 5, 4, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 5, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem5, 9, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 5, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem7, 6, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 4, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem8, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem9, 6, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 7, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem10, 5, 3, 1, 1)
        self.leftObliqueViewLowThreshField = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftObliqueViewLowThreshField.sizePolicy().hasHeightForWidth())
        self.leftObliqueViewLowThreshField.setSizePolicy(sizePolicy)
        self.leftObliqueViewLowThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.leftObliqueViewLowThreshField.setObjectName("leftObliqueViewLowThreshField")
        self.gridLayout_7.addWidget(self.leftObliqueViewLowThreshField, 5, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem11, 5, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 4, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem12, 9, 0, 1, 1)
        self.leftObliqueViewLowThreshSlider = QtWidgets.QSlider(self.groupBox_5)
        self.leftObliqueViewLowThreshSlider.setMaximum(255)
        self.leftObliqueViewLowThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.leftObliqueViewLowThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.leftObliqueViewLowThreshSlider.setTickInterval(1)
        self.leftObliqueViewLowThreshSlider.setObjectName("leftObliqueViewLowThreshSlider")
        self.gridLayout_7.addWidget(self.leftObliqueViewLowThreshSlider, 5, 4, 1, 2)
        self.leftObliqueViewEdgeAlgo = QtWidgets.QComboBox(self.groupBox_5)
        self.leftObliqueViewEdgeAlgo.setObjectName("leftObliqueViewEdgeAlgo")
        self.gridLayout_7.addWidget(self.leftObliqueViewEdgeAlgo, 2, 0, 1, 6)
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName("label_33")
        self.gridLayout_7.addWidget(self.label_33, 8, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setObjectName("label_35")
        self.gridLayout_7.addWidget(self.label_35, 7, 5, 1, 1, QtCore.Qt.AlignRight)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem13, 8, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem14, 8, 1, 1, 1)
        self.leftObliqueViewHighThreshSlider = QtWidgets.QSlider(self.groupBox_5)
        self.leftObliqueViewHighThreshSlider.setMaximum(255)
        self.leftObliqueViewHighThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.leftObliqueViewHighThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.leftObliqueViewHighThreshSlider.setTickInterval(1)
        self.leftObliqueViewHighThreshSlider.setObjectName("leftObliqueViewHighThreshSlider")
        self.gridLayout_7.addWidget(self.leftObliqueViewHighThreshSlider, 8, 4, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem15, 1, 0, 1, 1)
        self.leftObliqueViewHighThreshField = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftObliqueViewHighThreshField.sizePolicy().hasHeightForWidth())
        self.leftObliqueViewHighThreshField.setSizePolicy(sizePolicy)
        self.leftObliqueViewHighThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.leftObliqueViewHighThreshField.setObjectName("leftObliqueViewHighThreshField")
        self.gridLayout_7.addWidget(self.leftObliqueViewHighThreshField, 8, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem16, 11, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 5, 0, 1, 1)
        self.leftObliqueViewThreshApplyButton = QtWidgets.QPushButton(self.groupBox_5)
        self.leftObliqueViewThreshApplyButton.setObjectName("leftObliqueViewThreshApplyButton")
        self.gridLayout_7.addWidget(self.leftObliqueViewThreshApplyButton, 10, 4, 1, 1)
        self.leftObliqueViewEdgeImageLabel = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftObliqueViewEdgeImageLabel.sizePolicy().hasHeightForWidth())
        self.leftObliqueViewEdgeImageLabel.setSizePolicy(sizePolicy)
        self.leftObliqueViewEdgeImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.leftObliqueViewEdgeImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.leftObliqueViewEdgeImageLabel.setText("")
        self.leftObliqueViewEdgeImageLabel.setObjectName("leftObliqueViewEdgeImageLabel")
        self.gridLayout_7.addWidget(self.leftObliqueViewEdgeImageLabel, 0, 0, 1, 6, QtCore.Qt.AlignHCenter)
        self.label_26 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 4, 5, 1, 1, QtCore.Qt.AlignRight)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem17, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 13, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem18, 11, 0, 1, 12)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 9, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 10, 0, 1, 1)
        self.frontViewHighThreshField = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontViewHighThreshField.sizePolicy().hasHeightForWidth())
        self.frontViewHighThreshField.setSizePolicy(sizePolicy)
        self.frontViewHighThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.frontViewHighThreshField.setObjectName("frontViewHighThreshField")
        self.gridLayout_3.addWidget(self.frontViewHighThreshField, 13, 2, 1, 1)
        self.frontViewHighThreshSlider = QtWidgets.QSlider(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontViewHighThreshSlider.sizePolicy().hasHeightForWidth())
        self.frontViewHighThreshSlider.setSizePolicy(sizePolicy)
        self.frontViewHighThreshSlider.setMaximum(255)
        self.frontViewHighThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frontViewHighThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.frontViewHighThreshSlider.setTickInterval(1)
        self.frontViewHighThreshSlider.setObjectName("frontViewHighThreshSlider")
        self.gridLayout_3.addWidget(self.frontViewHighThreshSlider, 13, 4, 1, 8)
        self.frontViewThreshApplyButton = QtWidgets.QPushButton(self.groupBox)
        self.frontViewThreshApplyButton.setObjectName("frontViewThreshApplyButton")
        self.gridLayout_3.addWidget(self.frontViewThreshApplyButton, 15, 4, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem19, 16, 4, 1, 1)
        self.frontViewLowThreshSlider = QtWidgets.QSlider(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontViewLowThreshSlider.sizePolicy().hasHeightForWidth())
        self.frontViewLowThreshSlider.setSizePolicy(sizePolicy)
        self.frontViewLowThreshSlider.setMaximum(255)
        self.frontViewLowThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frontViewLowThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.frontViewLowThreshSlider.setTickInterval(1)
        self.frontViewLowThreshSlider.setObjectName("frontViewLowThreshSlider")
        self.gridLayout_3.addWidget(self.frontViewLowThreshSlider, 10, 4, 1, 8)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem20, 14, 0, 1, 12)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 13, 1, 1, 1)
        self.frontViewEdgeAlgo = QtWidgets.QComboBox(self.groupBox)
        self.frontViewEdgeAlgo.setObjectName("frontViewEdgeAlgo")
        self.gridLayout_3.addWidget(self.frontViewEdgeAlgo, 7, 0, 1, 12)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem22, 6, 0, 1, 12)
        spacerItem23 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem23, 13, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 12, 11, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 12, 4, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem24, 10, 1, 1, 1)
        self.frontViewEdgeImageLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontViewEdgeImageLabel.sizePolicy().hasHeightForWidth())
        self.frontViewEdgeImageLabel.setSizePolicy(sizePolicy)
        self.frontViewEdgeImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.frontViewEdgeImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frontViewEdgeImageLabel.setText("")
        self.frontViewEdgeImageLabel.setObjectName("frontViewEdgeImageLabel")
        self.gridLayout_3.addWidget(self.frontViewEdgeImageLabel, 0, 0, 6, 12)
        spacerItem25 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem25, 10, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 9, 11, 1, 1)
        self.frontViewLowThreshField = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frontViewLowThreshField.sizePolicy().hasHeightForWidth())
        self.frontViewLowThreshField.setSizePolicy(sizePolicy)
        self.frontViewLowThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.frontViewLowThreshField.setObjectName("frontViewLowThreshField")
        self.gridLayout_3.addWidget(self.frontViewLowThreshField, 10, 2, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem26, 8, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.backButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.backButton.setObjectName("backButton")
        self.gridLayout_2.addWidget(self.backButton, 6, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.leftLateralViewThreshApplyButton = QtWidgets.QPushButton(self.groupBox_3)
        self.leftLateralViewThreshApplyButton.setObjectName("leftLateralViewThreshApplyButton")
        self.gridLayout_5.addWidget(self.leftLateralViewThreshApplyButton, 11, 4, 1, 1)
        self.leftLateralViewHighThreshField = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftLateralViewHighThreshField.sizePolicy().hasHeightForWidth())
        self.leftLateralViewHighThreshField.setSizePolicy(sizePolicy)
        self.leftLateralViewHighThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.leftLateralViewHighThreshField.setObjectName("leftLateralViewHighThreshField")
        self.gridLayout_5.addWidget(self.leftLateralViewHighThreshField, 9, 2, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem27, 2, 4, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem28, 6, 1, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem29, 7, 3, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem30, 12, 3, 1, 1)
        self.leftLateralViewEdgeAlgo = QtWidgets.QComboBox(self.groupBox_3)
        self.leftLateralViewEdgeAlgo.setObjectName("leftLateralViewEdgeAlgo")
        self.gridLayout_5.addWidget(self.leftLateralViewEdgeAlgo, 3, 0, 1, 7)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 5, 4, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 8, 6, 1, 1)
        self.leftLateralViewHighThreshSlider = QtWidgets.QSlider(self.groupBox_3)
        self.leftLateralViewHighThreshSlider.setMaximum(255)
        self.leftLateralViewHighThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.leftLateralViewHighThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.leftLateralViewHighThreshSlider.setTickInterval(1)
        self.leftLateralViewHighThreshSlider.setObjectName("leftLateralViewHighThreshSlider")
        self.gridLayout_5.addWidget(self.leftLateralViewHighThreshSlider, 9, 4, 1, 3)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem31, 9, 1, 1, 1)
        self.leftLateralViewLowThreshSlider = QtWidgets.QSlider(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftLateralViewLowThreshSlider.sizePolicy().hasHeightForWidth())
        self.leftLateralViewLowThreshSlider.setSizePolicy(sizePolicy)
        self.leftLateralViewLowThreshSlider.setMaximum(255)
        self.leftLateralViewLowThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.leftLateralViewLowThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.leftLateralViewLowThreshSlider.setTickInterval(1)
        self.leftLateralViewLowThreshSlider.setObjectName("leftLateralViewLowThreshSlider")
        self.gridLayout_5.addWidget(self.leftLateralViewLowThreshSlider, 6, 4, 1, 3)
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 9, 0, 1, 1)
        self.leftLateralViewEdgeImageLabel = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftLateralViewEdgeImageLabel.sizePolicy().hasHeightForWidth())
        self.leftLateralViewEdgeImageLabel.setSizePolicy(sizePolicy)
        self.leftLateralViewEdgeImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.leftLateralViewEdgeImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.leftLateralViewEdgeImageLabel.setText("")
        self.leftLateralViewEdgeImageLabel.setObjectName("leftLateralViewEdgeImageLabel")
        self.gridLayout_5.addWidget(self.leftLateralViewEdgeImageLabel, 1, 0, 1, 7, QtCore.Qt.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 5, 6, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem32, 6, 3, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem33, 10, 3, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem34, 9, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 8, 4, 1, 1)
        self.leftLateralViewLowThreshField = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftLateralViewLowThreshField.sizePolicy().hasHeightForWidth())
        self.leftLateralViewLowThreshField.setSizePolicy(sizePolicy)
        self.leftLateralViewLowThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.leftLateralViewLowThreshField.setObjectName("leftLateralViewLowThreshField")
        self.gridLayout_5.addWidget(self.leftLateralViewLowThreshField, 6, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 6, 0, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem35, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 1, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem36, 3, 0, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem37, 5, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 11, 9, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 11, 10, 1, 1, QtCore.Qt.AlignRight)
        self.rightObliqueViewEdgeImageLabel = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightObliqueViewEdgeImageLabel.sizePolicy().hasHeightForWidth())
        self.rightObliqueViewEdgeImageLabel.setSizePolicy(sizePolicy)
        self.rightObliqueViewEdgeImageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.rightObliqueViewEdgeImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.rightObliqueViewEdgeImageLabel.setText("")
        self.rightObliqueViewEdgeImageLabel.setObjectName("rightObliqueViewEdgeImageLabel")
        self.gridLayout_6.addWidget(self.rightObliqueViewEdgeImageLabel, 0, 5, 1, 6, QtCore.Qt.AlignHCenter)
        spacerItem38 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem38, 13, 5, 1, 1)
        self.rightObliqueViewLowThreshField = QtWidgets.QLineEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightObliqueViewLowThreshField.sizePolicy().hasHeightForWidth())
        self.rightObliqueViewLowThreshField.setSizePolicy(sizePolicy)
        self.rightObliqueViewLowThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.rightObliqueViewLowThreshField.setObjectName("rightObliqueViewLowThreshField")
        self.gridLayout_6.addWidget(self.rightObliqueViewLowThreshField, 9, 7, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 8, 10, 1, 1, QtCore.Qt.AlignRight)
        spacerItem39 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem39, 5, 5, 1, 1)
        self.rightObliqueViewLowThreshSlider = QtWidgets.QSlider(self.groupBox_4)
        self.rightObliqueViewLowThreshSlider.setMaximum(255)
        self.rightObliqueViewLowThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rightObliqueViewLowThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rightObliqueViewLowThreshSlider.setTickInterval(1)
        self.rightObliqueViewLowThreshSlider.setObjectName("rightObliqueViewLowThreshSlider")
        self.gridLayout_6.addWidget(self.rightObliqueViewLowThreshSlider, 9, 9, 1, 2)
        spacerItem40 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem40, 10, 5, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem41, 12, 6, 1, 1)
        self.rightObliqueViewEdgeAlgo = QtWidgets.QComboBox(self.groupBox_4)
        self.rightObliqueViewEdgeAlgo.setObjectName("rightObliqueViewEdgeAlgo")
        self.gridLayout_6.addWidget(self.rightObliqueViewEdgeAlgo, 6, 5, 1, 6)
        spacerItem42 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem42, 9, 8, 1, 1)
        self.rightObliqueViewThreshApplyButton = QtWidgets.QPushButton(self.groupBox_4)
        self.rightObliqueViewThreshApplyButton.setObjectName("rightObliqueViewThreshApplyButton")
        self.gridLayout_6.addWidget(self.rightObliqueViewThreshApplyButton, 14, 9, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem43, 9, 6, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 8, 9, 1, 1)
        self.rightObliqueViewHighThreshField = QtWidgets.QLineEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightObliqueViewHighThreshField.sizePolicy().hasHeightForWidth())
        self.rightObliqueViewHighThreshField.setSizePolicy(sizePolicy)
        self.rightObliqueViewHighThreshField.setMaximumSize(QtCore.QSize(50, 30))
        self.rightObliqueViewHighThreshField.setObjectName("rightObliqueViewHighThreshField")
        self.gridLayout_6.addWidget(self.rightObliqueViewHighThreshField, 12, 7, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 9, 5, 1, 1)
        self.rightObliqueViewHighThreshSlider = QtWidgets.QSlider(self.groupBox_4)
        self.rightObliqueViewHighThreshSlider.setMaximum(255)
        self.rightObliqueViewHighThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rightObliqueViewHighThreshSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rightObliqueViewHighThreshSlider.setTickInterval(1)
        self.rightObliqueViewHighThreshSlider.setObjectName("rightObliqueViewHighThreshSlider")
        self.gridLayout_6.addWidget(self.rightObliqueViewHighThreshSlider, 12, 9, 1, 2)
        spacerItem44 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem44, 15, 5, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem45, 12, 8, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 12, 5, 1, 1)
        spacerItem46 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem46, 7, 5, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        edgeDetectionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(edgeDetectionWindow)
        self.statusbar.setObjectName("statusbar")
        edgeDetectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(edgeDetectionWindow)
        QtCore.QMetaObject.connectSlotsByName(edgeDetectionWindow)

        self.window = edgeDetectionWindow
        self.setupWidgets()
        self.updateImageLabels()

    def retranslateUi(self, edgeDetectionWindow):
        _translate = QtCore.QCoreApplication.translate
        edgeDetectionWindow.setWindowTitle(_translate("edgeDetectionWindow", "Edge Detection Screen"))
        self.nextButton.setText(_translate("edgeDetectionWindow", "Proceed to Next Window"))
        self.groupBox_2.setTitle(_translate("edgeDetectionWindow", "Right Lateral View"))
        self.label_15.setText(_translate("edgeDetectionWindow", "Low Threshold"))
        self.rightLateralViewThreshApplyButton.setText(_translate("edgeDetectionWindow", "Apply"))
        self.label_20.setText(_translate("edgeDetectionWindow", "255"))
        self.label_19.setText(_translate("edgeDetectionWindow", "0"))
        self.label_18.setText(_translate("edgeDetectionWindow", "High Threshold"))
        self.label_17.setText(_translate("edgeDetectionWindow", "255"))
        self.label_16.setText(_translate("edgeDetectionWindow", "0"))
        self.groupBox_5.setTitle(_translate("edgeDetectionWindow", "Left Oblique View"))
        self.label_34.setText(_translate("edgeDetectionWindow", "0"))
        self.label_25.setText(_translate("edgeDetectionWindow", "0"))
        self.label_33.setText(_translate("edgeDetectionWindow", "High Threshold"))
        self.label_35.setText(_translate("edgeDetectionWindow", "255"))
        self.label_24.setText(_translate("edgeDetectionWindow", "Low Threshold"))
        self.leftObliqueViewThreshApplyButton.setText(_translate("edgeDetectionWindow", "Apply"))
        self.label_26.setText(_translate("edgeDetectionWindow", "255"))
        self.groupBox.setTitle(_translate("edgeDetectionWindow", "Frontal View"))
        self.label_3.setText(_translate("edgeDetectionWindow", "High Threshold"))
        self.label_6.setText(_translate("edgeDetectionWindow", "0"))
        self.label_2.setText(_translate("edgeDetectionWindow", "Low Threshold"))
        self.frontViewThreshApplyButton.setText(_translate("edgeDetectionWindow", "Apply"))
        self.label_5.setText(_translate("edgeDetectionWindow", "255"))
        self.label_4.setText(_translate("edgeDetectionWindow", "0"))
        self.label_7.setText(_translate("edgeDetectionWindow", "255"))
        self.backButton.setText(_translate("edgeDetectionWindow", "Back"))
        self.groupBox_3.setTitle(_translate("edgeDetectionWindow", "Left Lateral View"))
        self.leftLateralViewThreshApplyButton.setText(_translate("edgeDetectionWindow", "Apply"))
        self.label_13.setText(_translate("edgeDetectionWindow", "0"))
        self.label_29.setText(_translate("edgeDetectionWindow", "255"))
        self.label_27.setText(_translate("edgeDetectionWindow", "High Threshold"))
        self.label_14.setText(_translate("edgeDetectionWindow", "255"))
        self.label_28.setText(_translate("edgeDetectionWindow", "0"))
        self.label_12.setText(_translate("edgeDetectionWindow", "Low Threshold"))
        self.groupBox_4.setTitle(_translate("edgeDetectionWindow", "Right Oblique View"))
        self.label_31.setText(_translate("edgeDetectionWindow", "0"))
        self.label_30.setText(_translate("edgeDetectionWindow", "255"))
        self.label_22.setText(_translate("edgeDetectionWindow", "255"))
        self.rightObliqueViewThreshApplyButton.setText(_translate("edgeDetectionWindow", "Apply"))
        self.label_32.setText(_translate("edgeDetectionWindow", "0"))
        self.label_21.setText(_translate("edgeDetectionWindow", "Low Threshold"))
        self.label_23.setText(_translate("edgeDetectionWindow", "High Threshold"))

    def setupWidgets(self):
        self.backButton.clicked.connect(lambda:self.buttonClicked(self.backButton, None))
        self.nextButton.clicked.connect(lambda:self.buttonClicked(self.nextButton, None))
        
        buttons = [self.frontViewThreshApplyButton, self.rightLateralViewThreshApplyButton, self.leftLateralViewThreshApplyButton, self.rightObliqueViewThreshApplyButton, self.leftObliqueViewThreshApplyButton]
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        for field1, field2 in fields:
            field1.clear()
            field2.clear()
            field1.setText("0")
            field2.setText("255")
        for slider1, slider2 in sliders:
            slider1.setValue(0)
            slider2.setValue(255)
        '''
        for i in range(len(sliders)):
            print(i)
            sliders[i][0].valueChanged.connect(lambda:self.sliderMoved(i,0))
            sliders[i][1].valueChanged.connect(lambda:self.sliderMoved(i,1))
            fields[i][0].textChanged.connect(lambda:self.fieldChanged(i,0))
            fields[i][1].textChanged.connect(lambda:self.fieldChanged(i,1))
        '''
        sliders[0][0].valueChanged.connect(lambda:self.sliderMoved(0,0))
        sliders[0][1].valueChanged.connect(lambda:self.sliderMoved(0,1))
        fields[0][0].textChanged.connect(lambda:self.fieldChanged(0,0))
        fields[0][1].textChanged.connect(lambda:self.fieldChanged(0,1))
        sliders[1][0].valueChanged.connect(lambda:self.sliderMoved(1,0))
        sliders[1][1].valueChanged.connect(lambda:self.sliderMoved(1,1))
        fields[1][0].textChanged.connect(lambda:self.fieldChanged(1,0))
        fields[1][1].textChanged.connect(lambda:self.fieldChanged(1,1))
        sliders[2][0].valueChanged.connect(lambda:self.sliderMoved(2,0))
        sliders[2][1].valueChanged.connect(lambda:self.sliderMoved(2,1))
        fields[2][0].textChanged.connect(lambda:self.fieldChanged(2,0))
        fields[2][1].textChanged.connect(lambda:self.fieldChanged(2,1))
        sliders[3][0].valueChanged.connect(lambda:self.sliderMoved(3,0))
        sliders[3][1].valueChanged.connect(lambda:self.sliderMoved(3,1))
        fields[3][0].textChanged.connect(lambda:self.fieldChanged(3,0))
        fields[3][1].textChanged.connect(lambda:self.fieldChanged(3,1))
        sliders[4][0].valueChanged.connect(lambda:self.sliderMoved(4,0))
        sliders[4][1].valueChanged.connect(lambda:self.sliderMoved(4,1))
        fields[4][0].textChanged.connect(lambda:self.fieldChanged(4,0))
        fields[4][1].textChanged.connect(lambda:self.fieldChanged(4,1))

        '''
        for i in range(len(buttons)):
            buttons[i].clicked.connect(lambda:self.buttonClicked(buttons[i], i))
        '''
        buttons[0].clicked.connect(lambda:self.buttonClicked(buttons[0], 0))
        buttons[1].clicked.connect(lambda:self.buttonClicked(buttons[1], 1))
        buttons[2].clicked.connect(lambda:self.buttonClicked(buttons[2], 2))
        buttons[3].clicked.connect(lambda:self.buttonClicked(buttons[3], 3))
        buttons[4].clicked.connect(lambda:self.buttonClicked(buttons[4], 4))

        self.edgeAlgos = ["Canny Edge Detector", "Sobel 3x3", "Laplacian 3x3", "Laplacian 5x5", "Prewitt", "Scharr"]
        self.frontViewEdgeAlgo.addItems(self.edgeAlgos)
        self.frontViewEdgeAlgo.setCurrentIndex(0)
        self.frontViewEdgeAlgo.currentIndexChanged.connect(lambda:self.edgeAlgoChanged(0))
        self.rightLateralViewEdgeAlgo.addItems(self.edgeAlgos)
        self.rightLateralViewEdgeAlgo.setCurrentIndex(0)
        self.rightLateralViewEdgeAlgo.currentIndexChanged.connect(lambda: self.edgeAlgoChanged(1))
        self.leftLateralViewEdgeAlgo.addItems(self.edgeAlgos)
        self.leftLateralViewEdgeAlgo.setCurrentIndex(0)
        self.leftLateralViewEdgeAlgo.currentIndexChanged.connect(lambda: self.edgeAlgoChanged(2))
        self.rightObliqueViewEdgeAlgo.addItems(self.edgeAlgos)
        self.rightObliqueViewEdgeAlgo.setCurrentIndex(0)
        self.rightObliqueViewEdgeAlgo.currentIndexChanged.connect(lambda: self.edgeAlgoChanged(3))
        self.leftObliqueViewEdgeAlgo.addItems(self.edgeAlgos)
        self.leftObliqueViewEdgeAlgo.setCurrentIndex(0)
        self.leftObliqueViewEdgeAlgo.currentIndexChanged.connect(lambda: self.edgeAlgoChanged(4))

        self.block = [True, True, True, True, True] # array to store value which represents wheather respective sliders can be unblocked

    def preprocessScreen(self):
        self.stallScreen()
        self.master = MasterThread(self.cache, self)
        self.master.createThreads()
        ret = self.master.startThreads()
        if ret is False:
            self.restoreScreen()

    def buttonClicked(self, button, idx = None):
        '''
            Tasks:
                check button if self.backButton or self.nextButton
                else do edge detection with help of index
                    use index to find respective button and block it
                    block self.backButton, self.nextButton
                    prepare thread and do edge detection on self.cache.roiMasks[idx] using self.cache.originalImages[idx]
                    prepare function to receive result with idx, and display it on respective label
                    unblock respective buttons
                    unblock self.backButton, self.nextButton
        '''
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        if button == self.backButton:
            self.window.close()
            window = self.window
            cache = self.cache
            del self.window
            del self.cache
            obj = AnomalyDetectionScreen.AnomalyDetectionScreen(window, cache)
            window.showMaximized()
            obj.preprocessScreen()
        elif button == self.nextButton:
            self.window.close()
            window = self.window
            cache = self.cache
            del self.window
            del self.cache
            RemarksScreen.RemarksScreen(window, cache)
            window.showMaximized()
        else:
            if self.cache.originalImages[idx] is not None and self.cache.roiMasks is not None:
                self.blockIdx(idx)
                boxes = [self.frontViewEdgeAlgo, self.rightLateralViewEdgeAlgo, self.leftLateralViewEdgeAlgo, self.rightObliqueViewEdgeAlgo, self.leftObliqueViewEdgeAlgo]
                if boxes[idx].currentText() == "Canny Edge Detector":
                    sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
                    # finding body edges using k-means method for k=2
                    k_means = self.KMeansBackgroundElimination(self.cache.originalImages[idx])
                    import cv2 as cv
                    body_edges = cv.Canny(k_means, 0, 255)
                    # finding edges in ROI using given thresholds
                    low = sliders[idx][0].value()
                    high = sliders[idx][1].value()
                    gray = cv.cvtColor(self.cache.roiMasks[idx], cv.COLOR_BGR2GRAY)
                    edges = cv.Canny(gray, low, high)
                    # OR both k-means output and Canny output to generate final result
                    result = cv.bitwise_or(body_edges, edges)
                    result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
                    self.cache.edges[idx][0] = result
                    self.cache.edges[idx][1] = low
                    self.cache.edges[idx][2] = high
                    self.updateEdgeImageLabel(idx)
                else:
                    import cv2 as cv
                    import numpy as np
                    from skimage.filters import sobel, scharr, prewitt, laplace
                    if boxes[idx].currentText() == "Sobel 3x3":
                        gray = cv.cvtColor(self.cache.originalImages[idx], cv.COLOR_BGR2GRAY)
                        filter = sobel(gray)
                        filter = filter / filter.max()
                        filter = filter * 255
                        filter = filter.astype(np.uint8)
                        result = filter.copy()
                        result *= 3
                        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
                        # cv.imshow('result',result)
                        # cv.waitKey()
                        self.cache.edges[idx][0] = result
                        self.updateEdgeImageLabel(idx)
                    elif boxes[idx].currentText() == "Laplacian 3x3":
                        gray = cv.cvtColor(self.cache.originalImages[idx], cv.COLOR_BGR2GRAY)
                        filter = laplace(gray)
                        filter = filter / filter.max()
                        filter = filter * 255
                        filter = filter.astype(np.uint8)
                        result = filter.copy()
                        result *= 1 # 3
                        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
                        # cv.imshow('result',result)
                        # cv.waitKey()
                        self.cache.edges[idx][0] = result
                        self.updateEdgeImageLabel(idx)
                    elif boxes[idx].currentText() == "Laplacian 5x5":
                        gray = cv.cvtColor(self.cache.originalImages[idx], cv.COLOR_BGR2GRAY)
                        filter = laplace(gray, ksize=5)
                        filter = filter / filter.max()
                        filter = filter * 255
                        filter = filter.astype(np.uint8)
                        result = filter.copy()
                        result *= 1 # 3
                        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
                        # cv.imshow('result',result)
                        # cv.waitKey()
                        self.cache.edges[idx][0] = result
                        self.updateEdgeImageLabel(idx)
                    elif boxes[idx].currentText() == "Prewitt":
                        gray = cv.cvtColor(self.cache.originalImages[idx], cv.COLOR_BGR2GRAY)
                        filter = prewitt(gray)
                        filter = filter / filter.max()
                        filter = filter * 255
                        filter = filter.astype(np.uint8)
                        result = filter.copy()
                        result *= 3
                        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
                        # cv.imshow('result',result)
                        # cv.waitKey()
                        self.cache.edges[idx][0] = result
                        self.updateEdgeImageLabel(idx)
                    elif boxes[idx].currentText() == "Scharr":
                        gray = cv.cvtColor(self.cache.originalImages[idx], cv.COLOR_BGR2GRAY)
                        filter = scharr(gray)
                        filter = filter / filter.max()
                        filter = filter * 255
                        filter = filter.astype(np.uint8)
                        result = filter.copy()
                        result *= 3
                        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
                        # cv.imshow('result',result)
                        # cv.waitKey()
                        self.cache.edges[idx][0] = result
                        self.updateEdgeImageLabel(idx)
                self.unblockIdx(idx)
                
    def edgeAlgoChanged(self, idx):
        boxes = [self.frontViewEdgeAlgo, self.rightLateralViewEdgeAlgo, self.leftLateralViewEdgeAlgo, self.rightObliqueViewEdgeAlgo, self.leftObliqueViewEdgeAlgo]
        if boxes[idx].currentText() == "Canny Edge Detector":
            self.block[idx] = True
            self.unblockSliders(idx)
        else:
            self.block[idx] = False
            self.blockSliders(idx)

    def blockSliders(self, idx):
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        sliders[idx][0].setEnabled(False)
        sliders[idx][1].setEnabled(False)
        fields[idx][0].setEnabled(False)
        fields[idx][1].setEnabled(False)

    def unblockSliders(self, idx):
        if self.block[idx] is True:
            sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
            fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
            sliders[idx][0].setEnabled(True)
            sliders[idx][1].setEnabled(True)
            fields[idx][0].setEnabled(True)
            fields[idx][1].setEnabled(True)

    def blockIdx(self, idx):
        self.blockButtons()
        buttons = [self.frontViewThreshApplyButton, self.rightLateralViewThreshApplyButton, self.leftLateralViewThreshApplyButton, self.rightObliqueViewThreshApplyButton, self.leftObliqueViewThreshApplyButton]
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        buttons[idx].setEnabled(False)
        #sliders[idx][0].setEnabled(False)
        #sliders[idx][1].setEnabled(False)
        #fields[idx][0].setEnabled(False)
        #fields[idx][1].setEnabled(False)
        self.blockSliders(idx)

    def unblockIdx(self, idx):
        self.unblockButtons()
        buttons = [self.frontViewThreshApplyButton, self.rightLateralViewThreshApplyButton, self.leftLateralViewThreshApplyButton, self.rightObliqueViewThreshApplyButton, self.leftObliqueViewThreshApplyButton]
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        buttons[idx].setEnabled(True)
        #sliders[idx][0].setEnabled(True)
        #sliders[idx][1].setEnabled(True)
        #fields[idx][0].setEnabled(True)
        #fields[idx][1].setEnabled(True)
        self.unblockSliders(idx)

    def blockButtons(self):
        self.backButton.setEnabled(False)
        self.nextButton.setEnabled(False)

    def unblockButtons(self):
        self.backButton.setEnabled(True)
        self.nextButton.setEnabled(True)

    def blockAll(self):
        self.blockButtons()
        buttons = [self.frontViewThreshApplyButton, self.rightLateralViewThreshApplyButton, self.leftLateralViewThreshApplyButton, self.rightObliqueViewThreshApplyButton, self.leftObliqueViewThreshApplyButton]
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        for i in range(len(sliders)):
            buttons[i].setEnabled(False)
            sliders[i][0].setEnabled(False)
            sliders[i][1].setEnabled(False)
            fields[i][0].setEnabled(False)
            fields[i][1].setEnabled(False)

    def unblockAll(self):
        self.unblockButtons()
        buttons = [self.frontViewThreshApplyButton, self.rightLateralViewThreshApplyButton, self.leftLateralViewThreshApplyButton, self.rightObliqueViewThreshApplyButton, self.leftObliqueViewThreshApplyButton]
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        for i in range(len(sliders)):
            buttons[i].setEnabled(True)
            sliders[i][0].setEnabled(True)
            sliders[i][1].setEnabled(True)
            fields[i][0].setEnabled(True)
            fields[i][1].setEnabled(True)

    def stallScreen(self):
        self.blockAll()
        self.progressBar.setEnabled(True)

    def restoreScreen(self):
        del self.master
        self.progressBar.setEnabled(False)
        self.unblockAll()

    def sliderMoved(self, idx1, idx2):
        #print("slider moved", idx1, idx2)
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        val = sliders[idx1][idx2].value()
        #print(val)
        fields[idx1][idx2].setText(str(val))

    def fieldChanged(self, idx1, idx2):
        #print("field changed", idx1, idx2)
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        string = fields[idx1][idx2].text()
        if len(string) < 1:
            return
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for char in string:
            if char not in numbers:
                return
        val = int(string)
        if val > 255:
            val = 255
        #print(val)
        sliders[idx1][idx2].setValue(val)
        self.sliderMoved(idx1, idx2)

    def updateImageLabels(self):
        #labels = [self.frontViewEdgeImageLabel, self.rightLateralViewEdgeImageLabel, self.leftLateralViewEdgeImageLabel, self.rightObliqueViewEdgeImageLabel, self.leftObliqueViewEdgeImageLabel]
        for i in range(len(self.cache.edges)):
            entry = self.cache.edges[i]
            if entry[0] is not None:
                #qimage = imageConversion(entry[0])
                #showOnWidget(labels[i], qimage)
                self.updateEdgeImageLabel(i)

    def updateEdgeImageLabel(self, idx):
        labels = [self.frontViewEdgeImageLabel, self.rightLateralViewEdgeImageLabel, self.leftLateralViewEdgeImageLabel, self.rightObliqueViewEdgeImageLabel, self.leftObliqueViewEdgeImageLabel]
        image = self.cache.edges[idx][0]
        low = self.cache.edges[idx][1]
        high = self.cache.edges[idx][2]
        qimage = imageConversion(image)
        showOnWidget(labels[idx], qimage)
        sliders = [[self.frontViewLowThreshSlider, self.frontViewHighThreshSlider], [self.rightLateralViewLowThreshSlider, self.rightLateralViewHighThreshSlider], [self.leftLateralViewLowThreshSlider, self.leftLateralViewHighThreshSlider], [self.rightObliqueViewLowThreshSlider, self.rightObliqueViewHighThreshSlider], [self.leftObliqueViewLowThreshSlider, self.leftObliqueViewHighThreshSlider]]
        fields = [[self.frontViewLowThreshField, self.frontViewHighThreshField], [self.rightLateralViewLowThreshField, self.rightLateralViewHighThreshField], [self.leftLateralViewLowThreshField, self.leftLateralViewHighThreshField], [self.rightObliqueViewLowThreshField, self.rightObliqueViewHighThreshField], [self.leftObliqueViewLowThreshField, self.leftObliqueViewHighThreshField]]
        fields[idx][0].clear()
        fields[idx][1].clear()
        fields[idx][0].setText(str(low))
        fields[idx][1].setText(str(high))
        sliders[idx][0].setValue(low)
        sliders[idx][1].setValue(high)

    def KMeansBackgroundElimination(self, img):
        import cv2 as cv
        import numpy as np
        
        k = 2
        image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        
        # converting RGB image matrix into array of float values for opencv kmeans procedure
        pixel_vals = image.reshape((-1,3))
        pixel_vals = np.float32(pixel_vals)
        
        # kmeans setup and execution
        # setting iterations to 100 and accuracy to 85%
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.85)
        # calling kmeans function of opencv
        retval, labels, centers = cv.kmeans(pixel_vals, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
        
        # converting segmentation result from float array to RGB matrix
        centers = np.uint8(centers)
        segmented_data = centers[labels.flatten()]
        segmented_image = segmented_data.reshape((image.shape))
        
        # converting result into Binary format (0(Black), 255(White))
        segmented_image = cv.cvtColor(segmented_image, cv.COLOR_RGB2BGR)
        segmented_gray_image = cv.cvtColor(segmented_image, cv.COLOR_BGR2GRAY)
        bwThresh, segmented_bw_image = cv.threshold(segmented_gray_image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        return segmented_bw_image

from PyQt5.QtCore import QThread, QObject, QMutex, pyqtSignal, pyqtSlot
import cv2 as cv
import numpy as np

class MasterThread:
    def __init__(self, cache, screen):
        self.cache = cache
        self.screen = screen
        self.objs = list()
        self.threads = list()
        self.mutex = QMutex()
        self.progress = 0
        self.incr = 20

    def createThreads(self):
        for i in range(len(self.cache.edges)):
            if self.cache.edges[i][0] is None and self.cache.originalImages[i] is not None and self.cache.roiMasks[i] is not None:
                obj = EdgeWorkerThread(i, self.cache.roiMasks[i], self.cache.originalImages[i], None, None, self.mutex)
                thread = QThread()
                obj.sendResult.connect(self.receiveResult)
                obj.moveToThread(thread)
                obj.finished.connect(thread.quit)
                thread.started.connect(obj.doWork)
                thread.finished.connect(self.checkThreads)
                self.objs.append(obj)
                self.threads.append(thread)
            else:
                self.objs.append(None)
                self.threads.append(None)
                self.progress += self.incr
                self.screen.progressBar.setValue(self.progress)

    def startThreads(self):
        ret = False
        for thread in self.threads:
            if thread is not None:
                ret = True
                thread.start()
        return ret

    def receiveResult(self, idx, low, high, image):
        self.cache.edges[idx][0] = image
        self.cache.edges[idx][1] = low
        self.cache.edges[idx][2] = high
        self.screen.updateEdgeImageLabel(idx)
        self.progress += self.incr
        self.screen.progressBar.setValue(self.progress)

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
        del self.progress
        del self.incr
        del self.mutex
        del self.cache
        del self.screen

class EdgeWorkerThread(QObject):
    finished = pyqtSignal()
    sendResult = pyqtSignal(int, int, int, np.ndarray)

    def __init__(self, idx, roi, original, low=None, high=None, mutex=None):
        super().__init__()
        self.idx = idx
        self.roi = roi
        self.low = low
        self.high = high
        self.original = original
        self.mutex = mutex

    def doWork(self):
        '''
        import cv2 as cv
        import numpy as np
        from skimage.filters import sobel, scharr, prewitt, laplace
        gray = cv.cvtColor(self.original, cv.COLOR_BGR2GRAY)
        sch = scharr(gray)
        sch = sch / sch.max()
        sch = sch * 255
        sch = sch.astype(np.uint8)
        result = sch.copy()
        result *= 3
        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
        #cv.imshow('result',result)
        #cv.waitKey()
        '''
        
        # generate body outline edges using k-means
        bodyOutline = self.KMeansBackgroundElimination(self.original)
        bodyOutlineEdges = cv.Canny(bodyOutline, 0, 255)
        # generating edges of ROI image
        grayRoi = cv.cvtColor(self.roi, cv.COLOR_BGR2GRAY)
        if self.low is None or self.high is None:
            highThresh, _ = cv.threshold(grayRoi, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
            highThresh = int(highThresh)
            lowThresh = int(0.5 * highThresh)
            self.low = lowThresh
            self.high = highThresh
        roiEdges = cv.Canny(grayRoi, self.low, self.high)
        # OR bodyOutlineEdges and roiEdges to generate result
        result = cv.bitwise_or(bodyOutlineEdges, roiEdges)
        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
        
        if self.mutex is not None:
            self.mutex.lock()
        self.sendResult.emit(self.idx, self.low, self.high, result)
        self.finished.emit()
        if self.mutex is not None:
            self.mutex.unlock()

    def KMeansBackgroundElimination(self, img):
        import cv2 as cv
        import numpy as np
        
        k = 2
        image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        
        # converting RGB image matrix into array of float values for opencv kmeans procedure
        pixel_vals = image.reshape((-1,3))
        pixel_vals = np.float32(pixel_vals)
        
        # kmeans setup and execution
        # setting iterations to 100 and accuracy to 85%
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.85)
        # calling kmeans function of opencv
        retval, labels, centers = cv.kmeans(pixel_vals, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
        
        # converting segmentation result from float array to RGB matrix
        centers = np.uint8(centers)
        segmented_data = centers[labels.flatten()]
        segmented_image = segmented_data.reshape((image.shape))
        
        # converting result into Binary format (0(Black), 255(White))
        segmented_image = cv.cvtColor(segmented_image, cv.COLOR_RGB2BGR)
        segmented_gray_image = cv.cvtColor(segmented_image, cv.COLOR_BGR2GRAY)
        bwThresh, segmented_bw_image = cv.threshold(segmented_gray_image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        return segmented_bw_image

    def __del__(self):
        #super().__del__()
        del self.idx
        del self.roi
        del self.low
        del self.high
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
##            image = cv.imread("thermal_image2.jpeg")
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
##        temp = cv.imread("yellow.jpg")
##        temp = cv.resize(temp, (640, 480), interpolation = cv.INTER_LANCZOS4)
##        cache.edges[3][0] = temp
##        cache.edges[3][1] = 25
##        cache.edges[3][2] = 80
##        return cache
##
##    @pyqtSlot()
##    def buttonWindow1_onClick(self):
##        self.close()
##        cache = self.generateCache()
##        self.obj = EdgeDetectionScreen(self, cache)
##        #self.show()
##        self.showMaximized()
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
    edgeDetectionWindow = QtWidgets.QMainWindow()
    ui = EdgeDetectionScreen()
    ui.setupUi(edgeDetectionWindow)
    edgeDetectionWindow.show()
    sys.exit(app.exec_())
'''
