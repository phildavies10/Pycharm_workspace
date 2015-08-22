# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayfacto_event.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(494, 431)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(155, 385, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWEditEvent = QtWidgets.QTabWidget(Dialog)
        self.tabWEditEvent.setGeometry(QtCore.QRect(15, 10, 471, 366))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWEditEvent.setFont(font)
        self.tabWEditEvent.setAutoFillBackground(False)
        self.tabWEditEvent.setStyleSheet("background-color:rgb(238, 238, 238)")
        self.tabWEditEvent.setObjectName("tabWEditEvent")
        self.tabBasic = QtWidgets.QWidget()
        self.tabBasic.setObjectName("tabBasic")
        self.labelNoDays = QtWidgets.QLabel(self.tabBasic)
        self.labelNoDays.setEnabled(False)
        self.labelNoDays.setGeometry(QtCore.QRect(300, 270, 96, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelNoDays.setFont(font)
        self.labelNoDays.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelNoDays.setObjectName("labelNoDays")
        self.checkBoxReminder = QtWidgets.QCheckBox(self.tabBasic)
        self.checkBoxReminder.setGeometry(QtCore.QRect(109, 265, 86, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxReminder.setFont(font)
        self.checkBoxReminder.setTristate(False)
        self.checkBoxReminder.setObjectName("checkBoxReminder")
        self.spinBoxNoDays = QtWidgets.QSpinBox(self.tabBasic)
        self.spinBoxNoDays.setEnabled(False)
        self.spinBoxNoDays.setGeometry(QtCore.QRect(210, 265, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBoxNoDays.setFont(font)
        self.spinBoxNoDays.setMaximum(365)
        self.spinBoxNoDays.setObjectName("spinBoxNoDays")
        self.dateEditStart = QtWidgets.QDateEdit(self.tabBasic)
        self.dateEditStart.setGeometry(QtCore.QRect(15, 190, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEditStart.setFont(font)
        self.dateEditStart.setCalendarPopup(True)
        self.dateEditStart.setObjectName("dateEditStart")
        self.labelCategory = QtWidgets.QLabel(self.tabBasic)
        self.labelCategory.setGeometry(QtCore.QRect(205, 165, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelCategory.setFont(font)
        self.labelCategory.setObjectName("labelCategory")
        self.comboBoxCategory = QtWidgets.QComboBox(self.tabBasic)
        self.comboBoxCategory.setGeometry(QtCore.QRect(205, 185, 246, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxCategory.setFont(font)
        self.comboBoxCategory.setEditable(False)
        self.comboBoxCategory.setCurrentText("")
        self.comboBoxCategory.setObjectName("comboBoxCategory")
        self.labelStartDate = QtWidgets.QLabel(self.tabBasic)
        self.labelStartDate.setGeometry(QtCore.QRect(15, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelStartDate.setFont(font)
        self.labelStartDate.setObjectName("labelStartDate")
        self.labelTitle = QtWidgets.QLabel(self.tabBasic)
        self.labelTitle.setGeometry(QtCore.QRect(205, 75, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.lineEditTitle = QtWidgets.QLineEdit(self.tabBasic)
        self.lineEditTitle.setGeometry(QtCore.QRect(10, 95, 446, 36))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lineEditTitle.setFont(font)
        self.lineEditTitle.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEditTitle.setText("")
        self.lineEditTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.labelBasic = QtWidgets.QLabel(self.tabBasic)
        self.labelBasic.setGeometry(QtCore.QRect(110, 15, 251, 46))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelBasic.setFont(font)
        self.labelBasic.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelBasic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelBasic.setScaledContents(False)
        self.labelBasic.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBasic.setObjectName("labelBasic")
        self.tabWEditEvent.addTab(self.tabBasic, "")
        self.tabRecurrence = QtWidgets.QWidget()
        self.tabRecurrence.setObjectName("tabRecurrence")
        self.labelRecurrence = QtWidgets.QLabel(self.tabRecurrence)
        self.labelRecurrence.setGeometry(QtCore.QRect(125, 15, 216, 46))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelRecurrence.setFont(font)
        self.labelRecurrence.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelRecurrence.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelRecurrence.setScaledContents(False)
        self.labelRecurrence.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRecurrence.setObjectName("labelRecurrence")
        self.radioButtonOneOff = QtWidgets.QRadioButton(self.tabRecurrence)
        self.radioButtonOneOff.setGeometry(QtCore.QRect(30, 80, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonOneOff.setFont(font)
        self.radioButtonOneOff.setChecked(True)
        self.radioButtonOneOff.setObjectName("radioButtonOneOff")
        self.radioButtonRecurring = QtWidgets.QRadioButton(self.tabRecurrence)
        self.radioButtonRecurring.setGeometry(QtCore.QRect(125, 80, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonRecurring.setFont(font)
        self.radioButtonRecurring.setObjectName("radioButtonRecurring")
        self.groupBoxDayOfMonth = QtWidgets.QGroupBox(self.tabRecurrence)
        self.groupBoxDayOfMonth.setEnabled(False)
        self.groupBoxDayOfMonth.setGeometry(QtCore.QRect(130, 225, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxDayOfMonth.setFont(font)
        self.groupBoxDayOfMonth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBoxDayOfMonth.setAutoFillBackground(False)
        self.groupBoxDayOfMonth.setTitle("")
        self.groupBoxDayOfMonth.setFlat(False)
        self.groupBoxDayOfMonth.setCheckable(False)
        self.groupBoxDayOfMonth.setObjectName("groupBoxDayOfMonth")
        self.radioButtonDayOfMonth2 = QtWidgets.QRadioButton(self.groupBoxDayOfMonth)
        self.radioButtonDayOfMonth2.setGeometry(QtCore.QRect(15, 45, 156, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonDayOfMonth2.setFont(font)
        self.radioButtonDayOfMonth2.setText("")
        self.radioButtonDayOfMonth2.setObjectName("radioButtonDayOfMonth2")
        self.radioButtonDayOfMonth1 = QtWidgets.QRadioButton(self.groupBoxDayOfMonth)
        self.radioButtonDayOfMonth1.setGeometry(QtCore.QRect(15, 25, 96, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonDayOfMonth1.setFont(font)
        self.radioButtonDayOfMonth1.setText("")
        self.radioButtonDayOfMonth1.setObjectName("radioButtonDayOfMonth1")
        self.groupBoxEvery = QtWidgets.QGroupBox(self.tabRecurrence)
        self.groupBoxEvery.setEnabled(False)
        self.groupBoxEvery.setGeometry(QtCore.QRect(15, 165, 106, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxEvery.setFont(font)
        self.groupBoxEvery.setTitle("")
        self.groupBoxEvery.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.groupBoxEvery.setObjectName("groupBoxEvery")
        self.radioButtonYears = QtWidgets.QRadioButton(self.groupBoxEvery)
        self.radioButtonYears.setGeometry(QtCore.QRect(25, 105, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonYears.setFont(font)
        self.radioButtonYears.setObjectName("radioButtonYears")
        self.radioButtonWeeks = QtWidgets.QRadioButton(self.groupBoxEvery)
        self.radioButtonWeeks.setEnabled(False)
        self.radioButtonWeeks.setGeometry(QtCore.QRect(25, 65, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonWeeks.setFont(font)
        self.radioButtonWeeks.setObjectName("radioButtonWeeks")
        self.radioButtonDays = QtWidgets.QRadioButton(self.groupBoxEvery)
        self.radioButtonDays.setEnabled(False)
        self.radioButtonDays.setGeometry(QtCore.QRect(25, 45, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonDays.setFont(font)
        self.radioButtonDays.setChecked(True)
        self.radioButtonDays.setObjectName("radioButtonDays")
        self.radioButtonMonths = QtWidgets.QRadioButton(self.groupBoxEvery)
        self.radioButtonMonths.setGeometry(QtCore.QRect(25, 85, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonMonths.setFont(font)
        self.radioButtonMonths.setObjectName("radioButtonMonths")
        self.spinBoxPeriod = QtWidgets.QSpinBox(self.groupBoxEvery)
        self.spinBoxPeriod.setGeometry(QtCore.QRect(25, 10, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxPeriod.setFont(font)
        self.spinBoxPeriod.setMinimum(0)
        self.spinBoxPeriod.setMaximum(999)
        self.spinBoxPeriod.setProperty("value", 0)
        self.spinBoxPeriod.setDisplayIntegerBase(10)
        self.spinBoxPeriod.setObjectName("spinBoxPeriod")
        self.labelEvery = QtWidgets.QLabel(self.tabRecurrence)
        self.labelEvery.setEnabled(False)
        self.labelEvery.setGeometry(QtCore.QRect(35, 145, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEvery.setFont(font)
        self.labelEvery.setObjectName("labelEvery")
        self.groupBoxTimes = QtWidgets.QGroupBox(self.tabRecurrence)
        self.groupBoxTimes.setEnabled(True)
        self.groupBoxTimes.setGeometry(QtCore.QRect(305, 170, 146, 136))
        self.groupBoxTimes.setTitle("")
        self.groupBoxTimes.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.groupBoxTimes.setObjectName("groupBoxTimes")
        self.dateEditFinishDate = QtWidgets.QDateEdit(self.groupBoxTimes)
        self.dateEditFinishDate.setEnabled(True)
        self.dateEditFinishDate.setGeometry(QtCore.QRect(20, 95, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEditFinishDate.setFont(font)
        self.dateEditFinishDate.setCalendarPopup(True)
        self.dateEditFinishDate.setObjectName("dateEditFinishDate")
        self.spinBoxNoOfTimes = QtWidgets.QSpinBox(self.groupBoxTimes)
        self.spinBoxNoOfTimes.setEnabled(True)
        self.spinBoxNoOfTimes.setGeometry(QtCore.QRect(20, 30, 42, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxNoOfTimes.setFont(font)
        self.spinBoxNoOfTimes.setMinimum(0)
        self.spinBoxNoOfTimes.setMaximum(999)
        self.spinBoxNoOfTimes.setProperty("value", 1)
        self.spinBoxNoOfTimes.setObjectName("spinBoxNoOfTimes")
        self.labelFinishDate = QtWidgets.QLabel(self.groupBoxTimes)
        self.labelFinishDate.setEnabled(True)
        self.labelFinishDate.setGeometry(QtCore.QRect(20, 75, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelFinishDate.setFont(font)
        self.labelFinishDate.setObjectName("labelFinishDate")
        self.labelNoOfTimes = QtWidgets.QLabel(self.groupBoxTimes)
        self.labelNoOfTimes.setEnabled(True)
        self.labelNoOfTimes.setGeometry(QtCore.QRect(20, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNoOfTimes.setFont(font)
        self.labelNoOfTimes.setObjectName("labelNoOfTimes")
        self.tabWEditEvent.addTab(self.tabRecurrence, "")
        self.tabAdditional = QtWidgets.QWidget()
        self.tabAdditional.setObjectName("tabAdditional")
        self.label_6 = QtWidgets.QLabel(self.tabAdditional)
        self.label_6.setGeometry(QtCore.QRect(135, 15, 196, 46))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.textEditNotes = QtWidgets.QTextEdit(self.tabAdditional)
        self.textEditNotes.setGeometry(QtCore.QRect(35, 95, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditNotes.setFont(font)
        self.textEditNotes.setFrameShape(QtWidgets.QFrame.Panel)
        self.textEditNotes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEditNotes.setLineWidth(1)
        self.textEditNotes.setMidLineWidth(5)
        self.textEditNotes.setAcceptRichText(False)
        self.textEditNotes.setObjectName("textEditNotes")
        self.label = QtWidgets.QLabel(self.tabAdditional)
        self.label.setGeometry(QtCore.QRect(35, 75, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateEditDob = QtWidgets.QDateEdit(self.tabAdditional)
        self.dateEditDob.setEnabled(False)
        self.dateEditDob.setGeometry(QtCore.QRect(35, 245, 110, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEditDob.setFont(font)
        self.dateEditDob.setCalendarPopup(True)
        self.dateEditDob.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEditDob.setObjectName("dateEditDob")
        self.checkBoxDOB = QtWidgets.QCheckBox(self.tabAdditional)
        self.checkBoxDOB.setGeometry(QtCore.QRect(35, 215, 70, 17))
        self.checkBoxDOB.setObjectName("checkBoxDOB")
        self.tabWEditEvent.addTab(self.tabAdditional, "")

        self.retranslateUi(Dialog)
        self.tabWEditEvent.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelNoDays.setText(_translate("Dialog", "No. of days"))
        self.checkBoxReminder.setText(_translate("Dialog", "Reminder"))
        self.spinBoxNoDays.setSuffix(_translate("Dialog", " days"))
        self.labelCategory.setText(_translate("Dialog", "Category"))
        self.labelStartDate.setText(_translate("Dialog", "Date"))
        self.labelTitle.setText(_translate("Dialog", "Event title"))
        self.lineEditTitle.setPlaceholderText(_translate("Dialog", "Title"))
        self.labelBasic.setText(_translate("Dialog", "Event settings"))
        self.tabWEditEvent.setTabText(self.tabWEditEvent.indexOf(self.tabBasic), _translate("Dialog", "Basic"))
        self.labelRecurrence.setText(_translate("Dialog", "Recurrence settings"))
        self.radioButtonOneOff.setText(_translate("Dialog", "One-off"))
        self.radioButtonRecurring.setText(_translate("Dialog", "Recurring"))
        self.radioButtonYears.setText(_translate("Dialog", "Year(s)"))
        self.radioButtonWeeks.setText(_translate("Dialog", "Week(s)"))
        self.radioButtonDays.setText(_translate("Dialog", "Day(s)"))
        self.radioButtonMonths.setText(_translate("Dialog", "Month(s)"))
        self.labelEvery.setText(_translate("Dialog", "Every:"))
        self.labelFinishDate.setText(_translate("Dialog", "Finish date"))
        self.labelNoOfTimes.setText(_translate("Dialog", "No. of times"))
        self.tabWEditEvent.setTabText(self.tabWEditEvent.indexOf(self.tabRecurrence), _translate("Dialog", "Recurrence"))
        self.label_6.setText(_translate("Dialog", "Additional settings"))
        self.label.setText(_translate("Dialog", "Notes"))
        self.checkBoxDOB.setText(_translate("Dialog", "D.O.B."))
        self.tabWEditEvent.setTabText(self.tabWEditEvent.indexOf(self.tabAdditional), _translate("Dialog", "Additional"))

