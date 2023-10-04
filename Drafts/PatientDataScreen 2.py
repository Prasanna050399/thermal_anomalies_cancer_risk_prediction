# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patientScreenEfMFjO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_patientDataScreenWindow(object):
    def setupUi(self, patientDataScreenWindow):
        if patientDataScreenWindow.objectName():
            patientDataScreenWindow.setObjectName(u"patientDataScreenWindow")
        patientDataScreenWindow.resize(1200, 600)
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(11)
        patientDataScreenWindow.setFont(font)
        self.centralwidget = QWidget(patientDataScreenWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -726, 1664, 1260))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.backButton = QPushButton(self.scrollAreaWidgetContents)
        self.backButton.setObjectName(u"backButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.backButton, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.patientInfoSection = QGroupBox(self.scrollAreaWidgetContents)
        self.patientInfoSection.setObjectName(u"patientInfoSection")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.patientInfoSection.sizePolicy().hasHeightForWidth())
        self.patientInfoSection.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        self.patientInfoSection.setFont(font1)
        self.patientInfoSection.setFlat(False)
        self.patientInfoSection.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.patientInfoSection)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.breastFeedingHistoryField = QComboBox(self.patientInfoSection)
        self.breastFeedingHistoryField.setObjectName(u"breastFeedingHistoryField")

        self.gridLayout_3.addWidget(self.breastFeedingHistoryField, 5, 4, 1, 4)

        self.patientIdField = QLineEdit(self.patientInfoSection)
        self.patientIdField.setObjectName(u"patientIdField")
        self.patientIdField.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.patientIdField.sizePolicy().hasHeightForWidth())
        self.patientIdField.setSizePolicy(sizePolicy2)
        self.patientIdField.setFont(font1)
        self.patientIdField.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.patientIdField, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 7, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 5, 8, 1, 1)

        self.patientDateOfBirthField = QDateEdit(self.patientInfoSection)
        self.patientDateOfBirthField.setObjectName(u"patientDateOfBirthField")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.patientDateOfBirthField.sizePolicy().hasHeightForWidth())
        self.patientDateOfBirthField.setSizePolicy(sizePolicy3)
        self.patientDateOfBirthField.setFont(font1)
        self.patientDateOfBirthField.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.patientDateOfBirthField, 3, 4, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 9, 2, 1, 1)

        self.ageDuringFirstPregnancyLabel = QLabel(self.patientInfoSection)
        self.ageDuringFirstPregnancyLabel.setObjectName(u"ageDuringFirstPregnancyLabel")
        sizePolicy.setHeightForWidth(self.ageDuringFirstPregnancyLabel.sizePolicy().hasHeightForWidth())
        self.ageDuringFirstPregnancyLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.ageDuringFirstPregnancyLabel, 5, 9, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.breastProfileField = QComboBox(self.patientInfoSection)
        self.breastProfileField.setObjectName(u"breastProfileField")

        self.gridLayout_3.addWidget(self.breastProfileField, 7, 10, 1, 1)

        self.mobileNumberField = QLineEdit(self.patientInfoSection)
        self.mobileNumberField.setObjectName(u"mobileNumberField")

        self.gridLayout_3.addWidget(self.mobileNumberField, 3, 10, 1, 1)

        self.referredByField = QLineEdit(self.patientInfoSection)
        self.referredByField.setObjectName(u"referredByField")
        self.referredByField.setMinimumSize(QSize(400, 30))
        self.referredByField.setMaximumSize(QSize(400, 30))
        self.referredByField.setFont(font1)

        self.gridLayout_3.addWidget(self.referredByField, 1, 4, 1, 4)

        self.radiationHistoryField = QComboBox(self.patientInfoSection)
        self.radiationHistoryField.setObjectName(u"radiationHistoryField")

        self.gridLayout_3.addWidget(self.radiationHistoryField, 9, 1, 1, 1)

        self.medicineConsumptionHistoryLabel = QLabel(self.patientInfoSection)
        self.medicineConsumptionHistoryLabel.setObjectName(u"medicineConsumptionHistoryLabel")
        sizePolicy.setHeightForWidth(self.medicineConsumptionHistoryLabel.sizePolicy().hasHeightForWidth())
        self.medicineConsumptionHistoryLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.medicineConsumptionHistoryLabel, 9, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_9, 7, 8, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.referredByLabel = QLabel(self.patientInfoSection)
        self.referredByLabel.setObjectName(u"referredByLabel")
        sizePolicy.setHeightForWidth(self.referredByLabel.sizePolicy().hasHeightForWidth())
        self.referredByLabel.setSizePolicy(sizePolicy)
        self.referredByLabel.setFont(font1)

        self.gridLayout_3.addWidget(self.referredByLabel, 1, 3, 1, 1, Qt.AlignHCenter)

        self.currentDatelabel = QLabel(self.patientInfoSection)
        self.currentDatelabel.setObjectName(u"currentDatelabel")
        sizePolicy.setHeightForWidth(self.currentDatelabel.sizePolicy().hasHeightForWidth())
        self.currentDatelabel.setSizePolicy(sizePolicy)
        self.currentDatelabel.setMinimumSize(QSize(0, 0))
        self.currentDatelabel.setFont(font1)

        self.gridLayout_3.addWidget(self.currentDatelabel, 1, 9, 1, 1, Qt.AlignHCenter)

        self.breastProfileLabel = QLabel(self.patientInfoSection)
        self.breastProfileLabel.setObjectName(u"breastProfileLabel")
        sizePolicy.setHeightForWidth(self.breastProfileLabel.sizePolicy().hasHeightForWidth())
        self.breastProfileLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.breastProfileLabel, 7, 9, 1, 1, Qt.AlignHCenter)

        self.selfHistoryOfBCField = QComboBox(self.patientInfoSection)
        self.selfHistoryOfBCField.setObjectName(u"selfHistoryOfBCField")

        self.gridLayout_3.addWidget(self.selfHistoryOfBCField, 7, 4, 1, 4)

        self.patientNameLabel = QLabel(self.patientInfoSection)
        self.patientNameLabel.setObjectName(u"patientNameLabel")
        sizePolicy.setHeightForWidth(self.patientNameLabel.sizePolicy().hasHeightForWidth())
        self.patientNameLabel.setSizePolicy(sizePolicy)
        self.patientNameLabel.setFont(font1)
        self.patientNameLabel.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout_3.addWidget(self.patientNameLabel, 3, 0, 1, 1, Qt.AlignHCenter)

        self.ageField = QLineEdit(self.patientInfoSection)
        self.ageField.setObjectName(u"ageField")
        self.ageField.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.ageField.sizePolicy().hasHeightForWidth())
        self.ageField.setSizePolicy(sizePolicy3)
        self.ageField.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.ageField, 3, 7, 1, 1, Qt.AlignHCenter)

        self.bcFamilyHistoryField = QComboBox(self.patientInfoSection)
        self.bcFamilyHistoryField.setObjectName(u"bcFamilyHistoryField")

        self.gridLayout_3.addWidget(self.bcFamilyHistoryField, 7, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.ageLabel = QLabel(self.patientInfoSection)
        self.ageLabel.setObjectName(u"ageLabel")
        sizePolicy.setHeightForWidth(self.ageLabel.sizePolicy().hasHeightForWidth())
        self.ageLabel.setSizePolicy(sizePolicy)
        self.ageLabel.setFont(font1)

        self.gridLayout_3.addWidget(self.ageLabel, 3, 6, 1, 1, Qt.AlignHCenter)

        self.currentDateFIeld = QDateEdit(self.patientInfoSection)
        self.currentDateFIeld.setObjectName(u"currentDateFIeld")
        self.currentDateFIeld.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.currentDateFIeld.sizePolicy().hasHeightForWidth())
        self.currentDateFIeld.setSizePolicy(sizePolicy3)
        self.currentDateFIeld.setFont(font1)
        self.currentDateFIeld.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.currentDateFIeld, 1, 10, 1, 1)

        self.patientDateOfBirthLabel = QLabel(self.patientInfoSection)
        self.patientDateOfBirthLabel.setObjectName(u"patientDateOfBirthLabel")
        sizePolicy.setHeightForWidth(self.patientDateOfBirthLabel.sizePolicy().hasHeightForWidth())
        self.patientDateOfBirthLabel.setSizePolicy(sizePolicy)
        self.patientDateOfBirthLabel.setFont(font1)

        self.gridLayout_3.addWidget(self.patientDateOfBirthLabel, 3, 3, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_10, 0, 0, 1, 1)

        self.bcFamilyHistoryLabel = QLabel(self.patientInfoSection)
        self.bcFamilyHistoryLabel.setObjectName(u"bcFamilyHistoryLabel")
        sizePolicy.setHeightForWidth(self.bcFamilyHistoryLabel.sizePolicy().hasHeightForWidth())
        self.bcFamilyHistoryLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.bcFamilyHistoryLabel, 7, 0, 1, 1, Qt.AlignHCenter)

        self.maritalStatusLabel = QLabel(self.patientInfoSection)
        self.maritalStatusLabel.setObjectName(u"maritalStatusLabel")
        sizePolicy.setHeightForWidth(self.maritalStatusLabel.sizePolicy().hasHeightForWidth())
        self.maritalStatusLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.maritalStatusLabel, 5, 0, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 3, 8, 1, 1)

        self.specialRemarksField = QTextEdit(self.patientInfoSection)
        self.specialRemarksField.setObjectName(u"specialRemarksField")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.specialRemarksField.sizePolicy().hasHeightForWidth())
        self.specialRemarksField.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.specialRemarksField, 9, 10, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 8, 0, 1, 1)

        self.maritalStatusField = QComboBox(self.patientInfoSection)
        self.maritalStatusField.setObjectName(u"maritalStatusField")

        self.gridLayout_3.addWidget(self.maritalStatusField, 5, 1, 1, 1)

        self.selfHistoryOfBCLabel = QLabel(self.patientInfoSection)
        self.selfHistoryOfBCLabel.setObjectName(u"selfHistoryOfBCLabel")
        sizePolicy.setHeightForWidth(self.selfHistoryOfBCLabel.sizePolicy().hasHeightForWidth())
        self.selfHistoryOfBCLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.selfHistoryOfBCLabel, 7, 3, 1, 1, Qt.AlignHCenter)

        self.medicalHistoryMeterLabel = QLabel(self.patientInfoSection)
        self.medicalHistoryMeterLabel.setObjectName(u"medicalHistoryMeterLabel")
        self.medicalHistoryMeterLabel.setMinimumSize(QSize(200, 200))
        self.medicalHistoryMeterLabel.setMaximumSize(QSize(200, 200))
        self.medicalHistoryMeterLabel.setFrameShape(QFrame.Box)
        self.medicalHistoryMeterLabel.setLineWidth(2)
        self.medicalHistoryMeterLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.medicalHistoryMeterLabel, 10, 10, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 3, 5, 1, 1)

        self.medicineConsumptionHistoryField = QComboBox(self.patientInfoSection)
        self.medicineConsumptionHistoryField.setObjectName(u"medicineConsumptionHistoryField")

        self.gridLayout_3.addWidget(self.medicineConsumptionHistoryField, 9, 4, 1, 4)

        self.patientNameField = QLineEdit(self.patientInfoSection)
        self.patientNameField.setObjectName(u"patientNameField")
        self.patientNameField.setFont(font1)

        self.gridLayout_3.addWidget(self.patientNameField, 3, 1, 1, 1)

        self.mobileNumberLabel = QLabel(self.patientInfoSection)
        self.mobileNumberLabel.setObjectName(u"mobileNumberLabel")
        sizePolicy.setHeightForWidth(self.mobileNumberLabel.sizePolicy().hasHeightForWidth())
        self.mobileNumberLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.mobileNumberLabel, 3, 9, 1, 1, Qt.AlignHCenter)

        self.patientIdLabel = QLabel(self.patientInfoSection)
        self.patientIdLabel.setObjectName(u"patientIdLabel")
        sizePolicy.setHeightForWidth(self.patientIdLabel.sizePolicy().hasHeightForWidth())
        self.patientIdLabel.setSizePolicy(sizePolicy)
        self.patientIdLabel.setFont(font1)

        self.gridLayout_3.addWidget(self.patientIdLabel, 1, 0, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 5, 2, 1, 1)

        self.radiationHistoryLabel = QLabel(self.patientInfoSection)
        self.radiationHistoryLabel.setObjectName(u"radiationHistoryLabel")
        sizePolicy.setHeightForWidth(self.radiationHistoryLabel.sizePolicy().hasHeightForWidth())
        self.radiationHistoryLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.radiationHistoryLabel, 9, 0, 1, 1)

        self.specialRemarksLabel = QLabel(self.patientInfoSection)
        self.specialRemarksLabel.setObjectName(u"specialRemarksLabel")
        sizePolicy.setHeightForWidth(self.specialRemarksLabel.sizePolicy().hasHeightForWidth())
        self.specialRemarksLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.specialRemarksLabel, 9, 9, 1, 1, Qt.AlignHCenter)

        self.breastFeedingHistoryLabel = QLabel(self.patientInfoSection)
        self.breastFeedingHistoryLabel.setObjectName(u"breastFeedingHistoryLabel")
        sizePolicy.setHeightForWidth(self.breastFeedingHistoryLabel.sizePolicy().hasHeightForWidth())
        self.breastFeedingHistoryLabel.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.breastFeedingHistoryLabel, 5, 3, 1, 1, Qt.AlignHCenter)

        self.label_17 = QLabel(self.patientInfoSection)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(300, 200))
        self.label_17.setMaximumSize(QSize(300, 200))

        self.gridLayout_3.addWidget(self.label_17, 10, 1, 1, 1)

        self.ageDuringFirstPregnancyField = QComboBox(self.patientInfoSection)
        self.ageDuringFirstPregnancyField.setObjectName(u"ageDuringFirstPregnancyField")

        self.gridLayout_3.addWidget(self.ageDuringFirstPregnancyField, 5, 10, 1, 1)


        self.gridLayout_2.addWidget(self.patientInfoSection, 1, 0, 1, 4)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_12, 2, 0, 1, 1)

        self.patientDiagnosticSection = QGroupBox(self.scrollAreaWidgetContents)
        self.patientDiagnosticSection.setObjectName(u"patientDiagnosticSection")
        sizePolicy1.setHeightForWidth(self.patientDiagnosticSection.sizePolicy().hasHeightForWidth())
        self.patientDiagnosticSection.setSizePolicy(sizePolicy1)
        self.patientDiagnosticSection.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(11)
        font2.setItalic(False)
        self.patientDiagnosticSection.setFont(font2)
        self.gridLayout_4 = QGridLayout(self.patientDiagnosticSection)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.diagnosticBreastProfileField = QComboBox(self.patientDiagnosticSection)
        self.diagnosticBreastProfileField.setObjectName(u"diagnosticBreastProfileField")

        self.gridLayout_4.addWidget(self.diagnosticBreastProfileField, 5, 1, 1, 1)

        self.diagnostic1CLabel = QLabel(self.patientDiagnosticSection)
        self.diagnostic1CLabel.setObjectName(u"diagnostic1CLabel")
        sizePolicy.setHeightForWidth(self.diagnostic1CLabel.sizePolicy().hasHeightForWidth())
        self.diagnostic1CLabel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.diagnostic1CLabel, 3, 0, 1, 1, Qt.AlignHCenter)

        self.diagnosticAsymmetryLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticAsymmetryLabel.setObjectName(u"diagnosticAsymmetryLabel")
        sizePolicy.setHeightForWidth(self.diagnosticAsymmetryLabel.sizePolicy().hasHeightForWidth())
        self.diagnosticAsymmetryLabel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.diagnosticAsymmetryLabel, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 4, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 0, 0, 1, 1)

        self.diagnosticCurvePatternField = QComboBox(self.patientDiagnosticSection)
        self.diagnosticCurvePatternField.setObjectName(u"diagnosticCurvePatternField")

        self.gridLayout_4.addWidget(self.diagnosticCurvePatternField, 1, 4, 1, 1)

        self.diagnostic1CField = QComboBox(self.patientDiagnosticSection)
        self.diagnostic1CField.setObjectName(u"diagnostic1CField")

        self.gridLayout_4.addWidget(self.diagnostic1CField, 3, 1, 1, 1)

        self.diagnosticBreastProfileLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticBreastProfileLabel.setObjectName(u"diagnosticBreastProfileLabel")

        self.gridLayout_4.addWidget(self.diagnosticBreastProfileLabel, 5, 0, 1, 1)

        self.diagnosticPinpointField = QComboBox(self.patientDiagnosticSection)
        self.diagnosticPinpointField.setObjectName(u"diagnosticPinpointField")

        self.gridLayout_4.addWidget(self.diagnosticPinpointField, 3, 6, 1, 1)

        self.diagnosticMeterReadingLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticMeterReadingLabel.setObjectName(u"diagnosticMeterReadingLabel")
        sizePolicy.setHeightForWidth(self.diagnosticMeterReadingLabel.sizePolicy().hasHeightForWidth())
        self.diagnosticMeterReadingLabel.setSizePolicy(sizePolicy)
        self.diagnosticMeterReadingLabel.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.diagnosticMeterReadingLabel, 7, 5, 1, 1, Qt.AlignHCenter)

        self.diagnosticFUniqueLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticFUniqueLabel.setObjectName(u"diagnosticFUniqueLabel")
        sizePolicy.setHeightForWidth(self.diagnosticFUniqueLabel.sizePolicy().hasHeightForWidth())
        self.diagnosticFUniqueLabel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.diagnosticFUniqueLabel, 5, 5, 1, 1, Qt.AlignHCenter)

        self.diagnosticHyperthermiaLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticHyperthermiaLabel.setObjectName(u"diagnosticHyperthermiaLabel")
        sizePolicy.setHeightForWidth(self.diagnosticHyperthermiaLabel.sizePolicy().hasHeightForWidth())
        self.diagnosticHyperthermiaLabel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.diagnosticHyperthermiaLabel, 1, 5, 1, 1, Qt.AlignHCenter)

        self.diagnosticMeterReadingField = QLCDNumber(self.patientDiagnosticSection)
        self.diagnosticMeterReadingField.setObjectName(u"diagnosticMeterReadingField")
        sizePolicy.setHeightForWidth(self.diagnosticMeterReadingField.sizePolicy().hasHeightForWidth())
        self.diagnosticMeterReadingField.setSizePolicy(sizePolicy)
        self.diagnosticMeterReadingField.setMinimumSize(QSize(375, 100))
        self.diagnosticMeterReadingField.setFrameShape(QFrame.WinPanel)
        self.diagnosticMeterReadingField.setFrameShadow(QFrame.Plain)
        self.diagnosticMeterReadingField.setLineWidth(5)
        self.diagnosticMeterReadingField.setMidLineWidth(0)
        self.diagnosticMeterReadingField.setSmallDecimalPoint(False)
        self.diagnosticMeterReadingField.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.diagnosticMeterReadingField, 7, 6, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 6, 0, 1, 1)

        self.diagnosticAsymmetryField = QComboBox(self.patientDiagnosticSection)
        self.diagnosticAsymmetryField.setObjectName(u"diagnosticAsymmetryField")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.diagnosticAsymmetryField.sizePolicy().hasHeightForWidth())
        self.diagnosticAsymmetryField.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.diagnosticAsymmetryField, 1, 1, 1, 1)

        self.diagnosticFurrowLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticFurrowLabel.setObjectName(u"diagnosticFurrowLabel")
        sizePolicy.setHeightForWidth(self.diagnosticFurrowLabel.sizePolicy().hasHeightForWidth())
        self.diagnosticFurrowLabel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.diagnosticFurrowLabel, 3, 3, 1, 1, Qt.AlignHCenter)

        self.diagnosticPinpointLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticPinpointLabel.setObjectName(u"diagnosticPinpointLabel")
        sizePolicy.setHeightForWidth(self.diagnosticPinpointLabel.sizePolicy().hasHeightForWidth())
        self.diagnosticPinpointLabel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.diagnosticPinpointLabel, 3, 5, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_12 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 1, 2, 1, 1)

        self.diagnosticFUniqueField = QComboBox(self.patientDiagnosticSection)
        self.diagnosticFUniqueField.setObjectName(u"diagnosticFUniqueField")

        self.gridLayout_4.addWidget(self.diagnosticFUniqueField, 5, 6, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 5, 2, 1, 1)

        self.diagnosticFurrowField = QComboBox(self.patientDiagnosticSection)
        self.diagnosticFurrowField.setObjectName(u"diagnosticFurrowField")

        self.gridLayout_4.addWidget(self.diagnosticFurrowField, 3, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.diagnosticCurvePatternLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticCurvePatternLabel.setObjectName(u"diagnosticCurvePatternLabel")
        sizePolicy.setHeightForWidth(self.diagnosticCurvePatternLabel.sizePolicy().hasHeightForWidth())
        self.diagnosticCurvePatternLabel.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.diagnosticCurvePatternLabel, 1, 3, 1, 1)

        self.diagnosticAgeField = QComboBox(self.patientDiagnosticSection)
        self.diagnosticAgeField.setObjectName(u"diagnosticAgeField")

        self.gridLayout_4.addWidget(self.diagnosticAgeField, 5, 4, 1, 1)

        self.diagnosticHyperthermiaField = QComboBox(self.patientDiagnosticSection)
        self.diagnosticHyperthermiaField.setObjectName(u"diagnosticHyperthermiaField")
        self.diagnosticHyperthermiaField.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.diagnosticHyperthermiaField, 1, 6, 1, 1)

        self.diagnosticAgeLabel = QLabel(self.patientDiagnosticSection)
        self.diagnosticAgeLabel.setObjectName(u"diagnosticAgeLabel")

        self.gridLayout_4.addWidget(self.diagnosticAgeLabel, 5, 3, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_14 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_14, 3, 2, 1, 1)


        self.gridLayout_2.addWidget(self.patientDiagnosticSection, 3, 0, 1, 4)

        self.verticalSpacer_8 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 4, 2, 1, 1)

        self.loadImagesButton = QPushButton(self.scrollAreaWidgetContents)
        self.loadImagesButton.setObjectName(u"loadImagesButton")
        sizePolicy.setHeightForWidth(self.loadImagesButton.sizePolicy().hasHeightForWidth())
        self.loadImagesButton.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.loadImagesButton, 5, 2, 1, 1, Qt.AlignRight)

        self.saveInformationButton = QPushButton(self.scrollAreaWidgetContents)
        self.saveInformationButton.setObjectName(u"saveInformationButton")
        sizePolicy.setHeightForWidth(self.saveInformationButton.sizePolicy().hasHeightForWidth())
        self.saveInformationButton.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.saveInformationButton, 5, 1, 1, 1, Qt.AlignRight)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        patientDataScreenWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(patientDataScreenWindow)
        self.statusbar.setObjectName(u"statusbar")
        patientDataScreenWindow.setStatusBar(self.statusbar)

        self.retranslateUi(patientDataScreenWindow)

        QMetaObject.connectSlotsByName(patientDataScreenWindow)
    # setupUi

    def retranslateUi(self, patientDataScreenWindow):
        patientDataScreenWindow.setWindowTitle(QCoreApplication.translate("patientDataScreenWindow", u"Patient Data Screen", None))
        self.backButton.setText(QCoreApplication.translate("patientDataScreenWindow", u"Go back to Main Menu", None))
        self.patientInfoSection.setTitle(QCoreApplication.translate("patientDataScreenWindow", u"Patient Information Section", None))
        self.ageDuringFirstPregnancyLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Age during first Pregnancy", None))
        self.medicineConsumptionHistoryLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Medicine ConsumptionHistory", None))
        self.referredByLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Referred By", None))
        self.currentDatelabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Current Date", None))
        self.breastProfileLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Breast Profile", None))
        self.patientNameLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Patient Name", None))
        self.ageLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Age", None))
        self.patientDateOfBirthLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Date of Birth", None))
        self.bcFamilyHistoryLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"BC Family History", None))
        self.maritalStatusLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Marital Status", None))
        self.selfHistoryOfBCLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Self history of BC", None))
        self.medicalHistoryMeterLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Medical history meter\n"
"image holder label", None))
        self.mobileNumberLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Mobile Number", None))
        self.patientIdLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Patient ID", None))
        self.radiationHistoryLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Radiation History", None))
        self.specialRemarksLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Special Remarks", None))
        self.breastFeedingHistoryLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Breast Feeding History", None))
        self.label_17.setText("")
        self.patientDiagnosticSection.setTitle(QCoreApplication.translate("patientDataScreenWindow", u"Diagnostic Meter Section", None))
        self.diagnostic1CLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"1C", None))
        self.diagnosticAsymmetryLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Asymmetry", None))
        self.diagnosticBreastProfileLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Breast Profile", None))
        self.diagnosticMeterReadingLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Diagnostic Meter Reading", None))
        self.diagnosticFUniqueLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"F Unique", None))
        self.diagnosticHyperthermiaLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Hyperthermia", None))
        self.diagnosticFurrowLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Furrow", None))
        self.diagnosticPinpointLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Pinpoint", None))
        self.diagnosticCurvePatternLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Curve Pattern", None))
        self.diagnosticAgeLabel.setText(QCoreApplication.translate("patientDataScreenWindow", u"Age", None))
        self.loadImagesButton.setText(QCoreApplication.translate("patientDataScreenWindow", u"Proceed to Load Images", None))
        self.saveInformationButton.setText(QCoreApplication.translate("patientDataScreenWindow", u"Save Information", None))
    # retranslateUi

