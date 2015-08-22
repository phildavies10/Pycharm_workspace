# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayfacto_category.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogCategoryManager(object):
    def setupUi(self, DialogCategoryManager):
        DialogCategoryManager.setObjectName("DialogCategoryManager")
        DialogCategoryManager.resize(323, 615)
        self.listWidgetCategories = QtWidgets.QListWidget(DialogCategoryManager)
        self.listWidgetCategories.setGeometry(QtCore.QRect(10, 10, 301, 416))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidgetCategories.setFont(font)
        self.listWidgetCategories.setObjectName("listWidgetCategories")
        self.pushButtonDelete = QtWidgets.QPushButton(DialogCategoryManager)
        self.pushButtonDelete.setGeometry(QtCore.QRect(185, 450, 96, 23))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.radioButtonEdit = QtWidgets.QRadioButton(DialogCategoryManager)
        self.radioButtonEdit.setGeometry(QtCore.QRect(25, 505, 56, 23))
        self.radioButtonEdit.setChecked(True)
        self.radioButtonEdit.setObjectName("radioButtonEdit")
        self.radioButtonNew = QtWidgets.QRadioButton(DialogCategoryManager)
        self.radioButtonNew.setGeometry(QtCore.QRect(25, 530, 56, 23))
        self.radioButtonNew.setObjectName("radioButtonNew")
        self.pushButtonOK = QtWidgets.QPushButton(DialogCategoryManager)
        self.pushButtonOK.setGeometry(QtCore.QRect(75, 570, 61, 23))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCancel = QtWidgets.QPushButton(DialogCategoryManager)
        self.pushButtonCancel.setGeometry(QtCore.QRect(175, 570, 61, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.lineEditCategory = QtWidgets.QLineEdit(DialogCategoryManager)
        self.lineEditCategory.setGeometry(QtCore.QRect(105, 520, 181, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCategory.setFont(font)
        self.lineEditCategory.setObjectName("lineEditCategory")
        self.labelCategory = QtWidgets.QLabel(DialogCategoryManager)
        self.labelCategory.setGeometry(QtCore.QRect(105, 495, 76, 16))
        self.labelCategory.setObjectName("labelCategory")
        self.pushButtonSelectAll = QtWidgets.QPushButton(DialogCategoryManager)
        self.pushButtonSelectAll.setGeometry(QtCore.QRect(10, 450, 61, 23))
        self.pushButtonSelectAll.setObjectName("pushButtonSelectAll")
        self.pushButtonClearAll = QtWidgets.QPushButton(DialogCategoryManager)
        self.pushButtonClearAll.setGeometry(QtCore.QRect(80, 450, 61, 23))
        self.pushButtonClearAll.setObjectName("pushButtonClearAll")

        self.retranslateUi(DialogCategoryManager)
        QtCore.QMetaObject.connectSlotsByName(DialogCategoryManager)

    def retranslateUi(self, DialogCategoryManager):
        _translate = QtCore.QCoreApplication.translate
        DialogCategoryManager.setWindowTitle(_translate("DialogCategoryManager", "Category manager"))
        self.pushButtonDelete.setText(_translate("DialogCategoryManager", "Delete selected"))
        self.radioButtonEdit.setText(_translate("DialogCategoryManager", "Edit"))
        self.radioButtonNew.setText(_translate("DialogCategoryManager", "New"))
        self.pushButtonOK.setText(_translate("DialogCategoryManager", "OK"))
        self.pushButtonCancel.setText(_translate("DialogCategoryManager", "Cancel"))
        self.labelCategory.setText(_translate("DialogCategoryManager", "Edit Category"))
        self.pushButtonSelectAll.setText(_translate("DialogCategoryManager", "Select all"))
        self.pushButtonClearAll.setText(_translate("DialogCategoryManager", "Clear all"))

