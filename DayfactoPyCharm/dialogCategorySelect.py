__author__ = 'phil'

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QListWidgetItem
from categorySelect import Ui_DialogCategorySelect
from utilClasses import Glob as G

class CategorySelectDlg(QDialog, Ui_DialogCategorySelect):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.setupUi(self)
        for it in G.categoryList:
            item = QListWidgetItem(it, self.listWidgetCategories)
            if it in G.categorySet:
                item.setCheckState(2)
            else:
                item.setCheckState(0)
        catLen = len(G.categoryList)
        sg = self.geometry()
        pg = parent.geometry()
        self.lt = pg.left() + 900
        self.tp = pg.top() + 100
        self.w = sg.width()
        self.h = catLen*35
        bOfst = (catLen *-25) +410
        self.listWidgetCategories.setGeometry(10, 10, 216, catLen * 25)
        self.pushButtonSelectAll.setGeometry(15, 445 - bOfst, 61, 23)
        self.pushButtonClearAll.setGeometry(155, 445 - bOfst, 61, 23)
        self.pushButtonOK.setGeometry(35, 495 - bOfst, 61, 23)
        self.pushButtonCancel.setGeometry(125, 495 - bOfst, 61, 23)
        # print(lt, tp, w, h)
        self.setGeometry(self.lt, self.tp, self.w, self.h)
        self.listWidgetCategories.setCurrentRow(1)
        self.pushButtonOK.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.reject)
        self.pushButtonSelectAll.clicked.connect(self.selectAll)
        self.pushButtonClearAll.clicked.connect(self.clearAll)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return and self.lineEditCategory.hasFocus():
            it = self.listWidgetCategories.currentItem()

    def accept(self):
        categoryList = []
        for row in range(0, self.listWidgetCategories.count()):
            it = self.listWidgetCategories.item(row)
            if it.checkState() == 2:
                categoryList.append(it.text())
        G.categorySet = set(categoryList)
        # print(G.categorySet)
        QDialog.accept(self)

    def clearAll(self):
        for row in range(1, self.listWidgetCategories.count()):
            self.listWidgetCategories.item(row).setCheckState(0)

    def selectAll(self):
        for row in range(1, self.listWidgetCategories.count()):
            self.listWidgetCategories.item(row).setCheckState(2)

    def reject(self):
        QDialog.reject(self)



