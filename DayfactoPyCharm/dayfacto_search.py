# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayfacto_search.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogSearch(object):
    def setupUi(self, DialogSearch):
        DialogSearch.setObjectName("DialogSearch")
        DialogSearch.resize(532, 190)
        self.lineEditSeachTerm = QtWidgets.QLineEdit(DialogSearch)
        self.lineEditSeachTerm.setGeometry(QtCore.QRect(300, 25, 211, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditSeachTerm.setFont(font)
        self.lineEditSeachTerm.setObjectName("lineEditSeachTerm")
        self.dateEditStart = QtWidgets.QDateEdit(DialogSearch)
        self.dateEditStart.setGeometry(QtCore.QRect(90, 25, 110, 22))
        self.dateEditStart.setCalendarPopup(True)
        self.dateEditStart.setObjectName("dateEditStart")
        self.dateEditEnd = QtWidgets.QDateEdit(DialogSearch)
        self.dateEditEnd.setGeometry(QtCore.QRect(90, 75, 110, 22))
        self.dateEditEnd.setCalendarPopup(True)
        self.dateEditEnd.setObjectName("dateEditEnd")
        self.checkBoxCase = QtWidgets.QCheckBox(DialogSearch)
        self.checkBoxCase.setGeometry(QtCore.QRect(330, 80, 16, 17))
        self.checkBoxCase.setText("")
        self.checkBoxCase.setObjectName("checkBoxCase")
        self.pushButtonSearch = QtWidgets.QPushButton(DialogSearch)
        self.pushButtonSearch.setGeometry(QtCore.QRect(145, 135, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonClose = QtWidgets.QPushButton(DialogSearch)
        self.pushButtonClose.setGeometry(QtCore.QRect(275, 135, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonClose.setFont(font)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.labelStartDate = QtWidgets.QLabel(DialogSearch)
        self.labelStartDate.setGeometry(QtCore.QRect(21, 30, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelStartDate.setFont(font)
        self.labelStartDate.setObjectName("labelStartDate")
        self.labelEndDate = QtWidgets.QLabel(DialogSearch)
        self.labelEndDate.setGeometry(QtCore.QRect(21, 80, 66, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEndDate.setFont(font)
        self.labelEndDate.setObjectName("labelEndDate")
        self.labelSeachTerm = QtWidgets.QLabel(DialogSearch)
        self.labelSeachTerm.setGeometry(QtCore.QRect(220, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSeachTerm.setFont(font)
        self.labelSeachTerm.setObjectName("labelSeachTerm")
        self.labelCaseCheck = QtWidgets.QLabel(DialogSearch)
        self.labelCaseCheck.setGeometry(QtCore.QRect(220, 80, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCaseCheck.setFont(font)
        self.labelCaseCheck.setObjectName("labelCaseCheck")

        self.retranslateUi(DialogSearch)
        QtCore.QMetaObject.connectSlotsByName(DialogSearch)

    def retranslateUi(self, DialogSearch):
        _translate = QtCore.QCoreApplication.translate
        DialogSearch.setWindowTitle(_translate("DialogSearch", "Search entries"))
        self.pushButtonSearch.setText(_translate("DialogSearch", "Search"))
        self.pushButtonClose.setText(_translate("DialogSearch", "Close"))
        self.labelStartDate.setText(_translate("DialogSearch", "From date"))
        self.labelEndDate.setText(_translate("DialogSearch", "To date"))
        self.labelSeachTerm.setText(_translate("DialogSearch", "Search term"))
        self.labelCaseCheck.setText(_translate("DialogSearch", "Case sensitive"))

