# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayfacto_category_select.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogCategorySelect(object):
    def setupUi(self, DialogCategorySelect):
        DialogCategorySelect.setObjectName("DialogCategorySelect")
        DialogCategorySelect.resize(239, 528)
        DialogCategorySelect.setModal(False)
        self.listWidgetCategories = QtWidgets.QListWidget(DialogCategorySelect)
        self.listWidgetCategories.setGeometry(QtCore.QRect(10, 10, 216, 421))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidgetCategories.setFont(font)
        self.listWidgetCategories.setObjectName("listWidgetCategories")
        self.pushButtonOK = QtWidgets.QPushButton(DialogCategorySelect)
        self.pushButtonOK.setGeometry(QtCore.QRect(35, 495, 61, 23))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCancel = QtWidgets.QPushButton(DialogCategorySelect)
        self.pushButtonCancel.setGeometry(QtCore.QRect(125, 495, 61, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonSelectAll = QtWidgets.QPushButton(DialogCategorySelect)
        self.pushButtonSelectAll.setGeometry(QtCore.QRect(15, 455, 61, 23))
        self.pushButtonSelectAll.setObjectName("pushButtonSelectAll")
        self.pushButtonClearAll = QtWidgets.QPushButton(DialogCategorySelect)
        self.pushButtonClearAll.setGeometry(QtCore.QRect(155, 455, 61, 23))
        self.pushButtonClearAll.setObjectName("pushButtonClearAll")

        self.retranslateUi(DialogCategorySelect)
        QtCore.QMetaObject.connectSlotsByName(DialogCategorySelect)

    def retranslateUi(self, DialogCategorySelect):
        _translate = QtCore.QCoreApplication.translate
        DialogCategorySelect.setWindowTitle(_translate("DialogCategorySelect", "Categories to display"))
        self.pushButtonOK.setText(_translate("DialogCategorySelect", "OK"))
        self.pushButtonCancel.setText(_translate("DialogCategorySelect", "Cancel"))
        self.pushButtonSelectAll.setText(_translate("DialogCategorySelect", "Select all"))
        self.pushButtonClearAll.setText(_translate("DialogCategorySelect", "Clear all"))

