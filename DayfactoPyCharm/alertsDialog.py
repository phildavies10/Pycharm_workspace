from PyQt5.QtWidgets import QDialog
from dialogAlerts import Ui_alertsDialog
from viewsUtils import AlertsTableModel, AlertsTableDelegate
from utilClasses import Glob as G

header = ('  Upcoming events', 'Dates')

class AlertsDlg(QDialog, Ui_alertsDialog):
    def __init__(self, alertsList=None, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.alertsList = alertsList
        lLen = len(self.alertsList)
        # print(lLen)
        sg = self.geometry()
        pg = self.parent.geometry()
        self.lt = pg.left() - 300
        self.tp = pg.top() + 100
        self.w = sg.width()
        self.h = 100 + lLen * 32
        self.setGeometry(self.lt, self.tp, self.w, self.h)
        self.tableViewAlerts.setGeometry(5, 5, 411, lLen * 45)
        self.pushButtonOK.setGeometry(175, 110 + lLen * 4, 61, 23)
        # self.setGeometry(200, 290, w, h)
        self.alertsTableModel = AlertsTableModel(self.alertsList, header=header)
        self.tableViewAlerts.setModel(self.alertsTableModel)
        self.tableViewAlerts.setItemDelegate(AlertsTableDelegate(self))
        self.tableViewAlerts.setColumnWidth(0, 297)
        self.tableViewAlerts.setColumnWidth(1, 108)
        self.pushButtonOK.clicked.connect(self.accept)

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
        self.setGeometry(self.lt - 20, self.tp + 20, self.w - 25, self.h - 200)
        pass
