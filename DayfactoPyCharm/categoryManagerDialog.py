'''
Created on 18 Apr 2015

@author: phil
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QLineEdit
from dayfacto_category import Ui_DialogCategoryManager
from sqliteUtils import saveCategories
from utilClasses import Glob as G

class CategoryManagerDlg(QDialog, Ui_DialogCategoryManager):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.setupUi(self)
        for it in G.categoryList:
            item = QListWidgetItem(it, self.listWidgetCategories)
            item.setCheckState(0)
        self.listWidgetCategories.setCurrentRow(1)
        self.lineEditCategory.setText(self.listWidgetCategories.item(1).text())
        self.pushButtonOK.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.reject)
        self.listWidgetCategories.itemDoubleClicked.connect(self.editItem)
        self.radioButtonEdit.toggled.connect(self.editToggle)
        self.pushButtonDelete.clicked.connect(self.deleteCategories)
        self.pushButtonSelectAll.clicked.connect(self.selectAll)
        self.pushButtonClearAll.clicked.connect(self.clearAll)
        self.lineEditCategory.setFocus()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return and self.lineEditCategory.hasFocus():
            if self.radioButtonNew.isChecked():
                t = self.lineEditCategory.text()
                if t > '' and not self.listWidgetCategories.findItems(t, Qt.MatchExactly):
                    item = QListWidgetItem(t, self.listWidgetCategories)
                    item.setCheckState(0)
                    self.lineEditCategory.setText('')
            else:
                it = self.listWidgetCategories.currentItem()
                it.setText(self.lineEditCategory.text())
        QLineEdit.keyPressEvent(self.lineEditCategory, e)

    def accept(self):
        G.categoryList = []
        for row in range(0, self.listWidgetCategories.count()):
            it = self.listWidgetCategories.item(row)
            G.categoryList.append(it.text())
        G.categoryList.sort()
        saveCategories(G.categoryList)
        QDialog.accept(self)

    def clearAll(self):
        for row in range(1, self.listWidgetCategories.count()):
            self.listWidgetCategories.item(row).setCheckState(0)

    def selectAll(self):
        for row in range(1, self.listWidgetCategories.count()):
            self.listWidgetCategories.item(row).setCheckState(2)

    def reject(self):
        QDialog.reject(self)

    def editItem(self):
        self.lineEditCategory.setText(self.listWidgetCategories.currentItem().text())
        self.lineEditCategory.setFocus()
        self.radioButtonEdit.setChecked(True)

    def editToggle(self):
        if self.radioButtonNew.isChecked():
            self.lineEditCategory.clear()
            self.lineEditCategory.setFocus()

    def deleteCategories(self):
        count = self.listWidgetCategories.count()
        for row in range(count-1, 0, -1):
            it = self.listWidgetCategories.item(row)
            if it.checkState() == 2:     # Checked:
                self.listWidgetCategories.takeItem(row)

    def enter(self):
        print('Enter')
