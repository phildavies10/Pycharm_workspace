# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayfacto_reminders_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_remindersDialog(object):
    def setupUi(self, remindersDialog):
        remindersDialog.setObjectName("remindersDialog")
        remindersDialog.setEnabled(True)
        remindersDialog.resize(423, 516)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(remindersDialog.sizePolicy().hasHeightForWidth())
        remindersDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        remindersDialog.setFont(font)
        remindersDialog.setWindowOpacity(1.0)
        remindersDialog.setSizeGripEnabled(True)
        self.pushButtonOK = QtWidgets.QPushButton(remindersDialog)
        self.pushButtonOK.setGeometry(QtCore.QRect(175, 480, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonOK.setFont(font)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.tableViewUpcoming = QtWidgets.QTableView(remindersDialog)
        self.tableViewUpcoming.setGeometry(QtCore.QRect(5, 5, 411, 401))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableViewUpcoming.setFont(font)
        self.tableViewUpcoming.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableViewUpcoming.setObjectName("tableViewUpcoming")
        self.radioButtonMonth_1 = QtWidgets.QRadioButton(remindersDialog)
        self.radioButtonMonth_1.setGeometry(QtCore.QRect(20, 420, 141, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonMonth_1.sizePolicy().hasHeightForWidth())
        self.radioButtonMonth_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonMonth_1.setFont(font)
        self.radioButtonMonth_1.setChecked(True)
        self.radioButtonMonth_1.setObjectName("radioButtonMonth_1")
        self.radioButtonMonth_2 = QtWidgets.QRadioButton(remindersDialog)
        self.radioButtonMonth_2.setGeometry(QtCore.QRect(20, 445, 146, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonMonth_2.sizePolicy().hasHeightForWidth())
        self.radioButtonMonth_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonMonth_2.setFont(font)
        self.radioButtonMonth_2.setObjectName("radioButtonMonth_2")
        self.radioButtonMonth_4 = QtWidgets.QRadioButton(remindersDialog)
        self.radioButtonMonth_4.setGeometry(QtCore.QRect(255, 420, 146, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonMonth_4.sizePolicy().hasHeightForWidth())
        self.radioButtonMonth_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonMonth_4.setFont(font)
        self.radioButtonMonth_4.setObjectName("radioButtonMonth_4")
        self.radioButtonMonth_6 = QtWidgets.QRadioButton(remindersDialog)
        self.radioButtonMonth_6.setGeometry(QtCore.QRect(255, 445, 141, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonMonth_6.sizePolicy().hasHeightForWidth())
        self.radioButtonMonth_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonMonth_6.setFont(font)
        self.radioButtonMonth_6.setObjectName("radioButtonMonth_6")
        self.groupBox = QtWidgets.QGroupBox(remindersDialog)
        self.groupBox.setGeometry(QtCore.QRect(9, 415, 391, 56))
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.pushButtonOK.raise_()
        self.tableViewUpcoming.raise_()
        self.radioButtonMonth_1.raise_()
        self.radioButtonMonth_2.raise_()
        self.radioButtonMonth_4.raise_()
        self.radioButtonMonth_6.raise_()

        self.retranslateUi(remindersDialog)
        QtCore.QMetaObject.connectSlotsByName(remindersDialog)

    def retranslateUi(self, remindersDialog):
        _translate = QtCore.QCoreApplication.translate
        remindersDialog.setWindowTitle(_translate("remindersDialog", "Reminders"))
        self.pushButtonOK.setText(_translate("remindersDialog", "OK"))
        self.radioButtonMonth_1.setText(_translate("remindersDialog", "This month"))
        self.radioButtonMonth_2.setText(_translate("remindersDialog", "Next two months"))
        self.radioButtonMonth_4.setText(_translate("remindersDialog", "Next four months"))
        self.radioButtonMonth_6.setText(_translate("remindersDialog", "Next six months"))

