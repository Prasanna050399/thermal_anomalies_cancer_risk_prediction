# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remarksScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_remarksWindow(object):
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

    def retranslateUi(self, remarksWindow):
        _translate = QtCore.QCoreApplication.translate
        remarksWindow.setWindowTitle(_translate("remarksWindow", "Remarks of Radiologists"))
        self.backButton.setText(_translate("remarksWindow", "Back"))
        self.label.setText(_translate("remarksWindow", "Impression by Radiologists"))
        self.nextButton.setText(_translate("remarksWindow", "Proceed to Report Generation"))
        self.label_2.setText(_translate("remarksWindow", "Left Breast"))
        self.label_4.setText(_translate("remarksWindow", "Suggest"))
        self.label_3.setText(_translate("remarksWindow", "Right Breast"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remarksWindow = QtWidgets.QMainWindow()
    ui = Ui_remarksWindow()
    ui.setupUi(remarksWindow)
    remarksWindow.show()
    sys.exit(app.exec_())