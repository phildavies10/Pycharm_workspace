# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayfacto_alerts_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_alertsDialog(object):
    def setupUi(self, alertsDialog):
        alertsDialog.setObjectName("alertsDialog")
        alertsDialog.setEnabled(True)
        alertsDialog.resize(423, 478)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(alertsDialog.sizePolicy().hasHeightForWidth())
        alertsDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        alertsDialog.setFont(font)
        alertsDialog.setWindowOpacity(1.0)
        alertsDialog.setSizeGripEnabled(True)
        self.pushButtonOK = QtWidgets.QPushButton(alertsDialog)
        self.pushButtonOK.setGeometry(QtCore.QRect(180, 430, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonOK.setFont(font)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.tableViewAlerts = QtWidgets.QTableView(alertsDialog)
        self.tableViewAlerts.setGeometry(QtCore.QRect(5, 5, 411, 401))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableViewAlerts.setFont(font)
        self.tableViewAlerts.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableViewAlerts.setObjectName("tableViewAlerts")

        self.retranslateUi(alertsDialog)
        QtCore.QMetaObject.connectSlotsByName(alertsDialog)

    def retranslateUi(self, alertsDialog):
        _translate = QtCore.QCoreApplication.translate
        alertsDialog.setWindowTitle(_translate("alertsDialog", "Reminders"))
        self.pushButtonOK.setText(_translate("alertsDialog", "OK"))

