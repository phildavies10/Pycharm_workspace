__author__ = 'phil'

from PyQt5.QtWidgets import QDialog
from dayfacto_search import Ui_DialogSearch
from utilClasses import Glob as G

class SearchDialog(QDialog, Ui_DialogSearch):
    def __init__(self, value='', case=False, parent=None, fDate=G.journalStartDate,
                 tDate=G.journalEndDate):
        QDialog.__init__(self)
        self.setupUi(self)
        self.lineEditSeachTerm.setText(value)
        self.checkBoxCase.setChecked(case)
        self.pushButtonSearch.clicked.connect(self.accept)
        self.pushButtonClose.clicked.connect(self.close)
        self.dateEditStart.setDate(fDate)
        self.dateEditEnd.setDate(tDate)
        self.Ok = False

    def textValue(self):
        return self.lineEditSeachTerm.text()

    def case(self):
        return self.checkBoxCase.checkState()

    def fDate(self):
        return self.dateEditStart.date()

    def tDate(self):
        return self.dateEditEnd.date()

    def accept(self):
        QDialog.accept(self)

    def isOk(self):
        return self.Ok
        self.result = True

    def close(self):
        QDialog.close(self)
