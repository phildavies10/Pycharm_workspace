'''
Created on 18 Apr 2015

@author: phil
'''

from PyQt5.QtWidgets import QDialog
from datetime import date
from dayfacto_event import Ui_Dialog
from genUtils import monthWeekNo, getWeekDayName, ordinal, getMonthDayName
from utilClasses import Glob as G

(NA, DAYS, WEEKS, MONTHS, YEARS) = range(5)
(NA, MONTHDAY, MONTHWEEKDAY) = range(3)

calcPeriod = {1: 'self.radioButtonDays.setChecked(True)',
              2: 'self.radioButtonWeeks.setChecked(True)',
              3: 'self.radioButtonMonths.setChecked(True)',
              4: 'self.radioButtonYears.setChecked(True)',}

class EventEditDlg(QDialog, Ui_Dialog):
    def __init__(self, sDate, eData=None, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        global categories
        self.comboBoxCategory.addItems(G.categoryList)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.checkBoxReminder.stateChanged.connect(self.reminderCheck);
        self.checkBoxDOB.stateChanged.connect(self.DOBCheck);
        self.radioButtonRecurring.toggled.connect(self.recurringToggle);
        self.radioButtonDays.toggled.connect(self.rbPeriodToggle);
        self.radioButtonWeeks.toggled.connect(self.rbPeriodToggle);
        self.radioButtonMonths.toggled.connect(self.rbPeriodToggle);
        self.radioButtonYears.toggled.connect(self.rbPeriodToggle);
        self.groupBoxTimes.setEnabled(False)
        self.evData = {}
        self.sDate = sDate
        self.dayNo = self.sDate.weekday()
        if eData is not None and len(eData) > 1:
            self.evData = eData.copy()
            self.lineEditTitle.setText(self.evData["Title"])
            self.textEditNotes.setText(self.evData["Notes"])
            i = self.comboBoxCategory.findText(self.evData["Category"])
            self.comboBoxCategory.setCurrentIndex(i)
            self.dateEditStart.setDate(self.evData["StartDate"])
            self.dateEditFinishDate.setDate(self.evData["StartDate"])
            if self.evData["ReminderDays"] is not None:
                self.checkBoxReminder.setChecked(True)
                self.spinBoxNoDays.setEnabled(True)
                self.spinBoxNoDays.setValue(int(self.evData["ReminderDays"]))
                self.labelNoDays.setEnabled(True)
            if  self.evData["NoOfTimes"] > 0: #self.evData["PeriodValue"] > 0 and
                self.radioButtonRecurring.setChecked(True)
                self.recurringToggle()
                self.spinBoxPeriod.setValue(self.evData["PeriodValue"])
                self.spinBoxNoOfTimes.setValue(self.evData["NoOfTimes"])
                eval(calcPeriod[self.evData["Period"]])
                self.radioButtonRecurring.setChecked(True)
                self.rbPeriodToggle()
            if self.evData["DOB"] is not None:
                self.checkBoxDOB.setChecked(True)
                self.DOBCheck()
            self.sDate = self.evData["StartDate"]
        else:
            self.evData["Notes"] = ""
        self.dayNo = self.sDate.weekday()

    def DOBCheck(self):
        if self.checkBoxDOB.checkState():
            self.dateEditDob.setEnabled(True)
            self.dateEditDob.setDate(date.today())
        else:
            self.dateEditDob.setEnabled(False)


    def reminderCheck(self):
        if self.checkBoxReminder.checkState():
            self.spinBoxNoDays.setEnabled(True)
            self.labelNoDays.setEnabled(True)
        else:
            self.spinBoxNoDays.setEnabled(False)
            self.labelNoDays.setEnabled(False)
            self.spinBoxNoDays.setValue(0)


    def recurringToggle(self):
        if self.radioButtonRecurring.isChecked():
            self.groupBoxEvery.setEnabled(True)
            self.labelEvery.setEnabled(True)
            self.groupBoxTimes.setEnabled(True)
            self.radioButtonDays.setEnabled(True)
            self.radioButtonWeeks.setEnabled(True)
            self.spinBoxPeriod.setValue(1)
            self.spinBoxNoOfTimes.setValue(1)
        elif self.radioButtonOneOff.isChecked():
            self.groupBoxEvery.setEnabled(False)
            self.labelEvery.setEnabled(False)
            self.groupBoxTimes.setEnabled(False)
            self.spinBoxPeriod.setValue(0)
            self.spinBoxNoOfTimes.setValue(0)

    def rbPeriodToggle(self):
        if self.radioButtonWeeks.isChecked() or self.radioButtonDays.isChecked():
            self.groupBoxDayOfMonth.setEnabled(False)
            self.radioButtonDayOfMonth1.setText('')
            self.radioButtonDayOfMonth2.setText('')
        elif self.radioButtonMonths.isChecked():
            self.groupBoxDayOfMonth.setEnabled(True)
            self.radioButtonDayOfMonth1.setText('nth of month')
            self.radioButtonDayOfMonth2.setText('nth of '  )
        elif self.radioButtonYears.isChecked():
            self.groupBoxDayOfMonth.setEnabled(True)
            mwn = monthWeekNo(self.sDate)
            wdn = getWeekDayName(self.sDate)
            mName = getMonthDayName(self.sDate)
            self.radioButtonDayOfMonth1.setText(str(self.dayNo)+ordinal(self.dayNo) +' of ' +mName)
            self.radioButtonDayOfMonth2.setText(str(mwn)+ordinal(mwn)+' '+wdn+' of '+mName)

    def refreshRecurrencData(self):
        self.evData["PeriodValue"] = self.spinBoxPeriod.value()
        self.evData["NoOfTimes"] = self.spinBoxNoOfTimes.value()
        if self.radioButtonDays.isChecked():
            period = DAYS
        elif self.radioButtonWeeks.isChecked():
            period = WEEKS
        elif self.radioButtonMonths.isChecked():
            period = MONTHS
        elif self.radioButtonYears.isChecked():
            period = YEARS
        else:
            period = NA
        self.evData["Period"] = period
        if self.radioButtonDayOfMonth1.isChecked():
            monthDay = MONTHDAY
        elif self.radioButtonDayOfMonth2.isChecked():
            monthDay = MONTHWEEKDAY
        else:
            monthDay = NA
        self.evData["MonthDay"] = monthDay

    def accept(self):
        self.refreshRecurrencData()
        self.evData["Title"] = self.lineEditTitle.text()
        self.evData["Notes"] = self.textEditNotes.toPlainText()
        self.evData["Category"] = self.comboBoxCategory.currentText()
        self.evData["ReminderDays"] = self.spinBoxNoDays.value()
        self.evData["StartDate"] = self.dateEditStart.date().toPyDate()
        if self.checkBoxDOB.checkState():
            self.evData["DOB"] = self.dateEditDob.date().toPyDate()
        else:
            self.evData["DOB"] = None
        self.evData["CreationDate"] = date.today()
        EventEditDlg.eventData = self.evData
        QDialog.accept(self)
