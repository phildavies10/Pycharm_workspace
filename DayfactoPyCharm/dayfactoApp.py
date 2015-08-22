from datetime import datetime, date
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
import PyQt5.QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from alertsDialog import AlertsDlg
from categoryManagerDialog import CategoryManagerDlg
from dayfacto_main import Ui_MainWindow
from dialogCategorySelect import CategorySelectDlg
from remindersDialog import RemindersDlg
import sqliteUtils
import uiConnections
from viewsUtils import (WeekViewTableModel, WeekViewDelegate, DaysListModel,
    MonthViewTableModel, MonthViewDelegate, EntriesViewTableModel, EntriesViewDelegate,
    EventsViewTableModel, EventsViewDelegate)
import eventEditDialog
import genUtils
import utilClasses
from utilClasses import Glob as G
import icalendar_import_export

temp = sys.stdout
# sys.stdout = open('log.txt', 'a')

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

class Filter(QObject):
    def eventFilter(self, widget, event):
        return False

daysHeader = ('Date', 'Entry', 'Sort date')
weekHeader = ('Date', 'Entry', 'Events')
monthHeader = genUtils.week
vheader = genUtils.week
daysDirty = True
eventsHeader = ('Title', 'Category', 'Start', 'End', 'Period', 'Occurs', 'DOB', 'evNo',
                'Sort date')

class MyWindow(QMainWindow, Ui_MainWindow):
    selected_date = date.today()
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        uiConnections.actionsSetup(self)
        uiConnections.connectSetup(self)
        sshFile = "mainWindow.qss"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())
        # self.setGeometry(650, 90, 621, 611) #> right/ > up/ > wider?/ > taller?
        # self.textBrowserJournalEntry.setGeometry(265, 40, 321, 391)
        # self.menuImport_export = QMenu(self.menuOptions)
        # self.menuImport_export.setObjectName("menuImport_export")
        # self.menuImport_export.addAction(self.action_export_icalendar)
        self.textBrowserJournalEntry.setGeometry(15, 40, 570, 391)
        self.row_pointer = 1
        self.entries_dic = {}
        self.entries_list = []
        self.events_list = []
        self.daysEntries = []
        self.weekEntries = []
        self.monthEntries = []
        self.entriesList = []
        self.eventsList = []
        self.remindersList = []
        self.alertsList = []
        self.remindersDialog = None
        self.alertsDialog = None
        self.categorySelectDialog = None
        self.title = ''
        self.selected_date = date.today()
        G.tDate = self.selected_date
        G.fDate = parse('2000-01-01', dayfirst='false')
        self._filter = Filter()
        self.stackedWidget.setCurrentIndex(0)
        self.evData = {}
        self.labelMonthView.setStyleSheet(G.monthStyle)
        self.daysViewModel = DaysListModel(self.daysEntries, daysHeader)
        self.daysTableView.setModel(self.daysViewModel)
        self.daysTableView.setColumnWidth(0, 73)
        self.daysTableView.setColumnWidth(1, 343)
        self.daysTableView.hide()
        self.weekViewModel = WeekViewTableModel(self.weekEntries, weekHeader)
        self.tableViewWeekView.setModel(self.weekViewModel)
        self.tableViewWeekView.setItemDelegate(WeekViewDelegate(self))
        self.tableViewWeekView.setColumnWidth(0, 74)
        self.tableViewWeekView.setColumnWidth(1, 380)
        self.tableViewWeekView.setColumnWidth(2, 80)
        self.tableViewWeekView.setSelectionMode(0)
        self.tableViewWeekView.setSelectionBehavior(0)
        self.tableViewWeekView.setWordWrap(True)
        self.tableViewWeekView.setSizeAdjustPolicy(0)
        self.monthViewModel = MonthViewTableModel(self.weekEntries, monthHeader)
        self.tableViewMonthView.setModel(self.monthViewModel)
        self.tableViewMonthView.setItemDelegate(MonthViewDelegate(self))
        evDisplayHeight = 80
        self.tableViewMonthView.setRowHeight(1, evDisplayHeight)
        self.tableViewMonthView.setRowHeight(3, evDisplayHeight)
        self.tableViewMonthView.setRowHeight(5, evDisplayHeight)
        self.tableViewMonthView.setRowHeight(7, evDisplayHeight)
        self.tableViewMonthView.setRowHeight(9, evDisplayHeight)
        self.entriesViewModel = EntriesViewTableModel(self.entriesList, daysHeader)
        self.tableViewEntries.setModel(self.entriesViewModel)
        self.tableViewEntries.setItemDelegate(EntriesViewDelegate(self))
        self.tableViewEntries.setAlternatingRowColors(False)
        self.tableViewEntries.setColumnWidth(0, 70)
        self.tableViewEntries.setColumnWidth(1, 515)
        self.tableViewEntries.setSelectionMode(1)
        self.tableViewEntries.setSelectionBehavior(0)
        self.tableViewEntries.verticalHeader().setDefaultSectionSize(40)
        self.tableViewEntries.setSizeAdjustPolicy(0)
        self.tableViewEntries.setSortingEnabled(True)
        self.tableViewEntries.hideColumn(2)
        self.eventsViewModel = EventsViewTableModel(self.eventsList, eventsHeader)
        self.tableViewEvents.setModel(self.eventsViewModel)
        self.tableViewEvents.setItemDelegate(EventsViewDelegate(self))
        self.tableViewEvents.setColumnWidth(0, 160)
        self.tableViewEvents.setColumnWidth(1, 100)
        self.tableViewEvents.setColumnWidth(2, 75)
        self.tableViewEvents.setColumnWidth(3, 75)
        self.tableViewEvents.setColumnWidth(4, 50)
        self.tableViewEvents.setColumnWidth(5, 50)
        self.tableViewEvents.setColumnWidth(6, 75)
        self.tableViewEvents.setSelectionMode(1)
        self.tableViewEvents.setRowHeight(1, 2)
        self.tableViewEvents.setSizeAdjustPolicy(0)
        self.tableViewEvents.setSortingEnabled(True)
        self.tableViewEvents.hideColumn(7)
        self.tableViewEvents.hideColumn(8)
        self.textBrowserDBTitle.setAlignment(PyQt5.QtCore.Qt.AlignHCenter)
        self.tableViewEvents.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.listViewEvents.setContextMenuPolicy(Qt.ActionsContextMenu)
        # self.pushButtonBackDay.clicked.connect(self.on_pushButtonBackDay_clicked())

        utilClasses.configRead(self)
        if G.daysListFlag is True:
            self.textBrowserJournalEntry.setGeometry(265, 40, 321, 391)
            self.daysTableView.show()
        else:
            self.textBrowserJournalEntry.setGeometry(15, 40, 570, 391)
            self.daysTableView.hide()
        if G.loadLast:
            self.openFile(fd=G.lastFile)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return and self.daysTableView.hasFocus():
            self.on_daysTableView_Clicked()

    def closeEvent(self, event):
        if self.remindersDialog:
            self.remindersDialog.close()
        if self.categorySelectDialog:
            self.categorySelectDialog.close()
        event.accept()

    def toggleLoadLast(self):
        if G.loadLast is True:
            G.loadLast = False
            self.actionLoad_last.setCheckable(False)
        else:
            G.loadLast = True
            self.actionLoad_last.setCheckable(True)
        'log.txt'(PyQt5.flush())
        # print(G.loadLast)

    def setWDir(self):
        d = genUtils.setWDir()
        if genUtils.os.path.exists(d): G.workingDirectory = d

    def openFile(self, fd):
        if not fd:
            fileName = genUtils.getFile()[0]
        else:
            fileName = fd
        if genUtils.os.path.exists(fileName):
            G.lastFile = fileName
            sqliteUtils.dbInit(fileName)
            t = sqliteUtils.fetchDBInfo()
            self.title = t[0][0]
            self.textBrowserDBTitle.setText(self.title)
            eventEditDialog.G.categoryList.clear()
            for cat in t:
                eventEditDialog.G.categoryList.append(cat[1])
                eventEditDialog.G.categoryList.sort()
            self.update()
        G.lastFile = fileName
        # self.on_actionSave_config()

    def newJournal(self):
        saveName = genUtils.saveFile()[0]
        # saveName = genUtils.os.path.join(G.workingDirectory, saveName)
        genUtils.newJournal(self, saveName, parent=self)
        self.clearCurrent()
        self.openFile(saveName)

    def exportIcalendar(self):
        icalendar_import_export.writeIcs()

    def importIcalendar(self):
            icalendar_import_export.readIcs()

    def callback(self):
        print('This is Callback')

    def on_actionSave_config(self):
        # print('Options called')
        utilClasses.configWrite(self)

    def clearCurrent(self):
        G.categoryList.clear()
        G.entriesList.clear()
        G.eventsList.clear()
        self.entries_dic.clear()
        self.entries_list.clear()
        self.events_list.clear()
        self.daysEntries.clear()
        self.weekEntries.clear()
        self.monthEntries.clear()
        self.entriesList.clear()
        self.eventsList.clear()
        self.title = ''
        # self.openFile('newDayfacto_2.db')

    def update(self):
        global daysDirty, daysEntries
        ind = 0
        c = 0
        # print(self.selected_date)
        if True:#daysDirty == True:
            allEnts = sqliteUtils.fetchAllEntries()
            if allEnts:
                self.daysEntries.clear()
                for ent in allEnts:
                    self.daysEntries.append((parse(str(ent[0])).strftime("%d/%m/%Y"),
                                             ent[1]))
                    if (datetime.date(parse(str(ent[0])))
                            <= datetime.date(parse(str((self.selected_date))))):
                        ind = c
                    c += 1
            self.daysViewModel.setAllData(self.daysEntries)
            if ind > 0:
                index = self.daysViewModel.createIndex(ind, 0)
                self.daysTableView.setCurrentIndex(index)
            # daysDirty = False
        self.events_list = {}
        self.evData.clear()
        self.calendarSelectDate.setSelectedDate(self.selected_date)
        self.dateEdit.setDate(self.selected_date)
        self.textBrowserNotes.setText('')
        self.textBrowserReminder.setText('')
        self.textBrowserCategory.setText('')
        d = sqliteUtils.fetchEntry(self.selected_date)
        if d is not None:
            self.textBrowserJournalEntry.setText(d[0])
            if len(d['event_list']) > 0:
                l = eval(d['event_list'])
                m = list(l)
                for n in m:
                    e = sqliteUtils.fetchEvent(n)
                    if e is not None:
                        if e['Category'] in G.categorySet:
                            self.events_list[n] = e['title']
        else:
            self.textBrowserJournalEntry.setText('')
        if self.stackedWidget.currentIndex() == 1:
            self.updateWeekView()
        if self.stackedWidget.currentIndex() == 2:
            self.updateMonthView()
        self.populateList()
        self.labelSelectedDate.setText((self.selected_date).strftime(
                        "%A  %B  %d,  %Y"))
        self.updateMonthView()
        self.setWindowTitle('Dayfacto file:   ' + G.lastFile)

    def editTitle(self):
        titleDialog = utilClasses.CustomInputDialog(posx=50, posy=170, label='Enter title:',
                             title='Title editor', value=self.title, parent=self)
        ok = titleDialog.exec_()
        text = titleDialog.textValue()
        if ok and text != '':
            self.title = text
            self.textBrowserDBTitle.setText(self.title)
            sqliteUtils.setDBTitle(self.title)

    def keysDBTitle(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            self.textBrowserDBTitle.setReadOnly(True)

    def populateList(self, selectedEvent=None):
        self.listViewEvents.clear()
        if len(self.events_list) > 0:
            for k in self.events_list:
                self.listViewEvents.addItem(self.events_list.get(k))
            selected = self.listViewEvents.item(0)
            selected.setSelected(True)
            self.listViewEvents.setCurrentItem(selected)

    def on_daysTableView_Clicked(self):
        a = self.daysTableView.currentIndex().row()
        entry = self.daysViewModel.listdata[a]
        self.selected_date = datetime.date(parse(str(entry[0])))
        self.update()

    def on_weekView_dblClicked(self):
        a = self.tableViewWeekView.currentIndex().row()
        entry = self.weekViewModel.listdata[a]
        self.selected_date = parse(str(entry[0]), dayfirst='false')
        self.stackedWidget.setCurrentIndex(0)
        self.update()

    def on_tableViewEntries_dblClicked(self):
        a = self.tableViewEntries.currentIndex().row()
        d = self.entriesViewModel.listdata[a][0]
        self.selected_date = parse(str(d), dayfirst='false')
        self.stackedWidget.setCurrentIndex(0)
        self.update()

    def on_tableViewEvents_dblClicked(self):
        a = self.tableViewEvents.currentIndex().row()
        i = self.eventsViewModel.listdata[a]
        ev = sqliteUtils.fetchEvent(int(i[7]))
        self.evData["Title"] = ev[5]
        self.evData["Notes"] = ev[6]
        self.evData["Category"] = ev[7]
        self.evData["ReminderDays"] = ev[11]
        self.evData["StartDate"] = ev[1]
        self.evData["Period"] = ev[9]
        self.evData["PeriodValue"] = ev[12]
        self.evData["NoOfTimes"] = ev[10]
        self.evData["DOB"] = ev[3]
        self.evData["EventNumber"] = ev[0]
        evNo = ev[0]
        # print(self.evData)
        dialog = eventEditDialog.EventEditDlg(eData=self.evData, sDate=self.selected_date)
        dialog.dateEditStart.setDate(self.selected_date)
        if dialog.exec_():
            newData = eventEditDialog.EventEditDlg.eventData
            sqliteUtils.updateEvent(evNo, newData)
        self.update()

    def on_monthView_dblClicked(self):
        row = self.tableViewMonthView.currentIndex().row() // 2
        column = self.tableViewMonthView.currentIndex().column()
        a = column + (row)*7
        d = self.monthViewModel.monthDates[a]
        self.selected_date = d
        self.resetGeom()
        self.stackedWidget.setCurrentIndex(0)
        self.update()

    def on_item_changed(self, curr, prev):
        self.evData.clear()
        self.evData["EventNumber"] = 0
        if curr is not None:
            for k in self.events_list.keys():
                if curr.text() == self.events_list[k]:
                    e = sqliteUtils.fetchEvent(k)
                    if e is not None:
                        self.textBrowserCategory.setText(e[7])
                        self.textBrowserNotes.setText(e[6])
                        self.textBrowserReminder.setText(str(e[11]))
                        self.evData = {"EventNumber": int(e[0]),
                                       "Title": e[5],
                                       "Notes": e[6],
                                       "Category": e[7],
                                       "ReminderDays": e[11],
                                       "StartDate": e[1],
                                       "NoOfTimes": e[10],
                                       "PeriodValue": e[12],
                                       "MonthDay": e[8],
                                       "Period": e[9],
                                       "DOB": e[3],
                                       }

    def onTitleDblClicked(self):
        self.textBrowserDBTitle.setReadOnly(False)

    def on_listItem_dblClicked(self):
        self.editEvent()

    def toggleDaysList(self):
        if self.daysTableView.isHidden():
            self.textBrowserJournalEntry.setGeometry(265, 40, 321, 391)
            self.daysTableView.show()
            G.daysListFlag = True
        else:
            self.daysTableView.hide()
            self.textBrowserJournalEntry.setGeometry(15, 40, 570, 391)
            G.daysListFlag = False
        utilClasses.configWrite(self)

    def gotoEntry(self):
        a = self.tableViewEvents.currentIndex().row()
        i = self.eventsViewModel.listdata[a]
        ev = sqliteUtils.fetchEvent(int(i[7]))
        self.selected_date = parse(str(ev[1]), dayfirst='false')
        self.update()
        self.stackedWidget.setCurrentIndex(0)

    def editEvent(self):
        dialog = eventEditDialog.EventEditDlg(eData=self.evData, sDate=self.selected_date)
        dialog.dateEditStart.setDate(self.selected_date)
        if dialog.exec_():
            newData = eventEditDialog.EventEditDlg.eventData
            sqliteUtils.updateEvent(newData["EventNumber"], newData)
        self.update()

    def categoryManager(self):
        try:
            dialog = CategoryManagerDlg(self)
            if dialog.exec_():
                self.update()
        except:
            pass

    def categorySelect(self):
        try:
            self.categorySelectDialog = CategorySelectDlg(self)
            # self.categorySelectDialog.setModal(False)
            self.categorySelectDialog.show()
            self.update()
        except:
            pass

    def deleteEventView(self):
        a = self.tableViewEvents.currentIndex().row()
        i = self.eventsViewModel.listdata[a]
        self.deleteEvent(i)

    def deleteEvent(self, rid):
            # rid = self.evData["EventNumber"]
            sqliteUtils.populateEntry(rid, delete=True)
            sqliteUtils.removeEvent(rid)
            self.update()

    def toggleStack(self):
        if self.stackedWidget.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(1)
        elif self.stackedWidget.currentIndex() == 1:
            self.stackedWidget.setCurrentIndex(2)
        elif self.stackedWidget.currentIndex() == 2:
            self.stackedWidget.setCurrentIndex(3)
        elif self.stackedWidget.currentIndex() == 3:
            self.stackedWidget.setCurrentIndex(4)
        else:
            self.stackedWidget.setCurrentIndex(0)

    def updateMonthView(self):
        monthDates = sqliteUtils.monthViewInit(self.selected_date)
        daysList = []
        self.monthEntries.clear()
        for d in monthDates:
            daysList.append(d.day)
            self.monthEntries.append(sqliteUtils.getEventTitles(datetime.date(d)))
        self.labelMonthView.setText(self.selected_date.strftime('%B  %Y'))
        self.monthViewModel.setAllData(self.monthEntries, daysList, monthDates)

    @pyqtSlot()
    def on_toolButtonEntries_clicked(self):
        ent = list(sqliteUtils.fetchAllEntriesNoBlanks())
        self.updateEntriesList(ent)
        self.resetGeom()
        self.stackedWidget.setCurrentIndex(3)

    @pyqtSlot()
    def on_toolButtonEvents_clicked(self):
        ev = list(sqliteUtils.fetchAllEvents())
        self.updateEventsView(ev)
        self.resetGeom()
        self.stackedWidget.setCurrentIndex(4)

    @pyqtSlot()
    def on_toolButtonMonthView_clicked(self):
        self.updateMonthView()
        self.stackedWidget.setGeometry(150, 100, 745, 711)
        self.tableViewMonthView.setGeometry(10, 35, 720, 680)
        self.stackedWidget.setCurrentIndex(2)

    def updateWeekView(self):
        weekDates = sqliteUtils.weekViewInit(self.selected_date)
        self.weekEntries.clear()
        for d in weekDates:
            fDay = format(d.strftime('%A'), '<11')
            strfDate = d.strftime("%d/%m/%Y")
            fDate = ''.join(('\n', fDay, '\n\n', strfDate))
            e = sqliteUtils.fetchEntry(datetime.date(d))
            if e is not None:
                self.weekEntries.append((fDate, e[0], sqliteUtils.getEventTitles(datetime.date(d))))
            else:
                self.weekEntries.append((fDate, '', ''))
        weekNo = weekDates[0].isocalendar()[1]
        self.labelWeekView.setText('Week No. ' + str(weekNo))
        self.weekViewModel.setAllData(self.weekEntries)

    def updateEntriesList(self, ent): #Used by on_toolButtonEntries_clicked & searchEntries
        # try:
        self.entriesList.clear()
        self.entriesList = [(entry[0].strftime("%d/%m/%Y"), entry[1],
              entry[0].strftime("%Y-%m-%d")) for entry in ent]
        # if len(self.entriesList) <= 2:
        #     print(self.entriesList, '\n', L, sep='',end='\n\n')
        self.entriesViewModel.setAllData(self.entriesList)
        # except:

    def updateEventsView(self, ev):
        try:
            self.eventsList.clear()
            for event in ev:
                if event[1] in G.categorySet:
                    if not event[3]:
                        endDate = '------'
                    else:
                        endDate = event[3].strftime("%Y-%m-%d")
                    if not event[7]:
                        DOB = '------'
                    else:
                        DOB = event[7].strftime("%Y-%m-%d")
                    self.eventsList.append((event[0], event[1], \
                            event[2].strftime("%d/%m/%Y"), \
                            endDate, G.periods[event[4]], str(event[5]), \
                            DOB, str(event[8]), event[2].strftime("%Y-%m-%d")))
            self.eventsViewModel.setAllData(self.eventsList)
        except:
            pass

    @pyqtSlot()
    def on_toolButtonWeekView_clicked(self):
        self.updateWeekView()
        self.resetGeom()
        self.stackedWidget.setCurrentIndex(1)

    def resetGeom(self):
        self.stackedWidget.setGeometry(250, 100, 621, 611)
        self.tableViewMonthView.setGeometry(10, 35, 596, 566)

    def entriesSearch(self):
        genUtils.searchEntries(self, parent=self)
        self.update()

    def eventsSearch(self):
        G.eventsList = self.eventsList
        genUtils.searchEvents(self, parent=self)
        self.eventsList = G.eventsList
        self.eventsViewModel.setAllData(G.eventsList)
        self.update()

    def updateReminders(self):
        self.remindersList.clear()
        # self.remindersList = fetchReminders(date.today(),
#                  date.today() + relativedelta(months=+1))
        self.remindersList = sqliteUtils.fetchReminders(self.selected_date,
                self.selected_date + relativedelta(months=+G.remindersPeriod))  # use for testing
        return self.remindersList


    def showReminders(self):
        self.updateReminders()
        self.remindersDialog = RemindersDlg(self.remindersList, parent=self)
        # if self.remindersDialog is None:
        #     self.remindersDialog = RemindersDlg(self.remindersList, parent=self)
        # else:
        #     self.remindersDialog.upcomingTableModel.setAllData(self.remindersList)
        self.remindersDialog.setWindowTitle('Reminders')
        self.remindersDialog.show()

    def updateAlerts(self):
        self.alertsList.clear()
        # self.remindersList = fetchAlerts(date.today())
        self.alertsList = sqliteUtils.fetchAlerts(self.selected_date)
        return self.alertsList

    def showAlerts(self):
        self.updateAlerts()
        if self.alertsDialog is None:
            self.alertsDialog = AlertsDlg(self.alertsList, parent=self)
        else:
            self.alertsDialog.alertsTableModel.setAllData(self.alertsList)
        self.alertsDialog.setWindowTitle('Alerts')
        self.alertsDialog.show()

    @pyqtSlot()
    def on_toolButtonDayView_clicked(self):
        self.updateWeekView()
        self.resetGeom()
        self.stackedWidget.setCurrentIndex(0)

    @pyqtSlot()
    def on_toolButtonToggleStack_clicked(self):
        self.toggleStack()

    @pyqtSlot()
    def on_toolButtonEditEvent_clicked(self):
        self.editEvent()

    @pyqtSlot()
    def on_toolButtonCategories_clicked(self):
        self.categorySelect()

    @pyqtSlot()
    def on_toolButtonPurge_clicked(self):
        sqliteUtils.purgeEntries(date(2015, 5, 12))

    @pyqtSlot()
    def on_toolButtonDeleteEvent_clicked(self):
        rid = self.evData["EventNumber"]
        self.deleteEvent(rid)

    @pyqtSlot()
    def on_toolButtonNewEvent_clicked(self):
        dialog = eventEditDialog.EventEditDlg(sDate =self.selected_date)
        dialog.dateEditStart.setDate(self.selected_date)
        if dialog.exec_():
            newData = eventEditDialog.EventEditDlg.eventData
            sqliteUtils.insertEvent(newData)
        self.update()

    @pyqtSlot()
    def on_pushButtonSearchEntries_clicked(self):
        self.entriesSearch()

    @pyqtSlot()
    def on_pushButtonSearchEvents_clicked(self):
        self.eventsSearch()

    @pyqtSlot()
    def on_pushButtonClearEntry_clicked(self):
        global daysDirty
        self.textBrowserJournalEntry.setText('')
        # addEntry(self.selected_date, self.textBrowserJournalEntry.toPlainText())
        daysDirty = True
        # self.update()

    @pyqtSlot()
    def on_pushButtonSaveEntry_clicked(self):
        global daysDirty
        sqliteUtils.addEntry(self.selected_date, self.textBrowserJournalEntry.toPlainText())
        daysDirty = True
        self.update()

    @pyqtSlot()
    def on_pushButtonToday_clicked(self):
        self.selected_date = date.today()
        self.update()

    @pyqtSlot()
    def on_pushButtonFwdDay_clicked(self):
        self.selected_date = self.selected_date + relativedelta(days=+ 1)
        self.update()

    @pyqtSlot()
    def on_pushButtonBackDay_clicked(self):
        self.selected_date = self.selected_date + relativedelta(days=- 1)
        self.update()

    @pyqtSlot()
    def on_pushButtonFwdWeek_clicked(self):
        self.selected_date = self.selected_date + relativedelta(weeks=+ 1)
        self.update()

    @pyqtSlot()
    def on_pushButtonBackWeek_clicked(self):
        self.selected_date = self.selected_date + relativedelta(weeks=- 1)
        self.update()

    @pyqtSlot()
    def on_pushButtonBackMonth_clicked(self):
        self.selected_date = self.selected_date + relativedelta(months=- 1)
        self.update()

    @pyqtSlot()
    def on_pushButtonFwdMonth_clicked(self):
        self.selected_date = self.selected_date + relativedelta(months=+ 1)
        self.update()

    @pyqtSlot()
    def on_pushButtonFwdYear_clicked(self):
        self.selected_date = self.selected_date + relativedelta(years=+ 1)
        self.update()

    @pyqtSlot()
    def on_pushButtonBackYear_clicked(self):
        self.selected_date = self.selected_date + relativedelta(years=- 1)
        self.update()

    @pyqtSlot()
    def on_calendarSelectDate_selectionChanged(self):
        self.selected_date = self.calendarSelectDate.selectedDate().toPyDate()
        self.dateEdit.setDate(self.selected_date)
        self.update()

    @pyqtSlot()
    def on__dateEdit_dateChanged(self):
        self.selected_date = self.dateEdit.date().toPyDate()
        self.calendarSelectDate.setDate(self.selected_date)
        self.update()

# if __name__ == '__main__':
main()
