from PyQt5.QtWidgets import QDialog
from dialogReminders import Ui_remindersDialog
from viewsUtils import RemindersTableModel, RemindersTableDelegate
from utilClasses import Glob as G

header = ('  Upcoming events', 'Dates')

class RemindersDlg(QDialog, Ui_remindersDialog):
    def __init__(self, remindersList=None, parent=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.remindersList = remindersList
        sg = self.geometry()
        pg = self.parent.geometry()
        self.lt = pg.left()-300
        self.tp = pg.top() +100
        self.w = sg.width()
        self.layout()
            # self.setGeometry(200, 290, w, h)
        self.upcomingTableModel = RemindersTableModel(self.remindersList, header=header)
        self.tableViewUpcoming.setModel(self.upcomingTableModel)
        self.tableViewUpcoming.setItemDelegate(RemindersTableDelegate(self))
        self.tableViewUpcoming.setColumnWidth(0, 297)
        self.tableViewUpcoming.setColumnWidth(1, 108)
        self.pushButtonOK.clicked.connect(self.accept)
        self.radioButtonMonth_1.clicked.connect(self.setPeriod)
        self.radioButtonMonth_2.clicked.connect(self.setPeriod)
        self.radioButtonMonth_4.clicked.connect(self.setPeriod)
        self.radioButtonMonth_6.clicked.connect(self.setPeriod)

    def layout(self):
        self.lLen = len(self.remindersList)
        if self.lLen > 15:
            self.lLen = 15
        print(self.lLen)
        self.h = 140 + self.lLen * 32
        self.setGeometry(self.lt, self.tp, self.w, self.h + 20)
        self.tableViewUpcoming.setGeometry(5, 5, 411, self.lLen * 32)
        self.groupBox.setGeometry(9, -105 + self.h, 391, 60)
        self.pushButtonOK.setGeometry(175, -20 + self.h, 61, 23)
        self.radioButtonMonth_1.setGeometry(20, -100 + self.h, 141, 17)
        self.radioButtonMonth_2.setGeometry(20, -70 + self.h, 146, 17)
        self.radioButtonMonth_4.setGeometry(255, -100 + self.h, 146, 17)
        self.radioButtonMonth_6.setGeometry(255, -70 + self.h, 141, 17)

    def accept(self):
        QDialog.accept(self)

    def setPeriod(self):
        if self.radioButtonMonth_1.isChecked():
            G.remindersPeriod = 1
        elif self.radioButtonMonth_2.isChecked():
            G.remindersPeriod = 2
        elif self.radioButtonMonth_4.isChecked():
            G.remindersPeriod = 4
        elif self.radioButtonMonth_6.isChecked():
            G.remindersPeriod = 6
        # print(G.remindersPeriod)
        remindersList = self.parent.updateReminders()
        self.upcomingTableModel.setAllData(remindersList)

    def offsetPos(self):
        self.setGeometry(self.lt-20, self.tp+20, self.w-25, self.h-200)
        pass
