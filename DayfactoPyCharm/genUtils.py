from datetime import date
# from dayfactoApp import MyWindow
import os
import PyQt5
import sqlite3
from searchDialog import SearchDialog
from PyQt5.QtWidgets import QDialog, QFileDialog
import sqliteUtils
from utilClasses import Glob as G

week = ('Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday')

sweek = ('Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat',
        'Sun')

Month = ['Jan',
         'Feb',
         'Mar',
         'Apr',
         'May',
         'Jun',
         'Jul',
         'Aug',
         'Sep',
         'Oct',
         'Nov',
         'Dec']

# selectedDate = date(2015, 5, 10)

# class EventsSearch():
#     def __init__(self, parent=None):
#         self.parent = parent
#
def searchEvents(self, parent=None):
    self.searchEventsDialog = SearchDialog(value=G.eventText, case=G.searchEventsCase)
    self.searchEventsDialog.setWindowTitle("Search events")
    Ok = self.searchEventsDialog.exec()
    text = self.searchEventsDialog.textValue()
    case = self.searchEventsDialog.case()
    if Ok == QDialog.Accepted:
        G.eventText = text
        G.searchEventsCase = case
        G.fDateEvents = self.searchEventsDialog.fDate()
        G.tDateEvents = self.searchEventsDialog.tDate()
        evs = sqliteUtils.fetchEventsByDates(G.fDateEvents, G.tDateEvents, text,
                                             case=case)
        parent.updateEventsView(evs)

def searchEntries(self, parent=None):
    self.searchEntriesDialog = SearchDialog(value=G.entryText, case=G.searchEntriesCase)
    self.searchEntriesDialog.setWindowTitle("Search entries")
    Ok = self.searchEntriesDialog.exec()
    text = self.searchEntriesDialog.textValue()
    case = self.searchEntriesDialog.case()
    if Ok == QDialog.Accepted:
        G.entryText = text
        G.searchEntriesCase = case
        G.fDateEntries = self.searchEntriesDialog.fDate()
        G.tDateEntries = self.searchEntriesDialog.tDate()
        ents = sqliteUtils.fetchEntriesByDates(G.fDateEntries, G.tDateEntries, \
             text, case=case)
        # print('Ents: ', ents)
        parent.updateEntriesList(ents)

def newJournal(self, name, parent):
    self.parent = parent
    create = not os.path.exists(name)
    db = sqlite3.connect(name)
    if create:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE diary_events ("
                       "EventNumber INTEGER PRIMARY KEY ASC AUTOINCREMENT UNIQUE,"
                       "StartDate    DATE  NOT NULL,"
                       "EndDate      DATE,"
                       "CreationDate DATE,"
                       "Title        TEXT,"
                       "Notes        TEXT,"
                       "Category     TEXT NOT NULL,"
                       "MonthDay     INTEGER DEFAULT (0),"
                       "Period       INTEGER DEFAULT (1),"
                       "NoOfTimes    INTEGER DEFAULT (1),"
                       "ReminderDays INTEGER,"
                       "PeriodValue  INTEGER DEFAULT (1)"
                       ")")
        # db.commit()
        # print('done')
        cursor.execute("CREATE TABLE diary_entries ("
                       "entry_date    DATE  PRIMARY KEY UNIQUE ON CONFLICT FAIL,"
                       "journal_entry TEXT DEFAULT (''),"
                       "event_list    TEXT DEFAULT ('')"
                       ")")
        # db.commit()
        print('done')
        cursor.execute("CREATE TABLE categories ("
                       "catId   INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "name    TEXT,"
                       "catType TEXT,"
                       "DBTitle TEXT "
                       ")")
        # db.commit()
        cursor.execute("INSERT INTO categories (name, DBTitle) VALUES(?, ?)",
                       ('(None)','Empty journal'))
    db.commit()
    # self.parent.callback()
    # print('done')

def monthWeekNo(d):
    day_of_month = d.day
    return (day_of_month - 1) // 7 + 1

def getWeekDayName(d):
    return week[d.weekday()]

def ordinal(n):
    if n % 10 == 1:
        return 'st'
    if n%10 == 2:
        return 'nd'
    if n%10 == 3:
        return 'rd'
    else:
        return 'th'

def getMonthDayName(d):
    return Month[(d.month) -1]

# class Filter(QObject):
#     def eventFilter(self, widget, event):
#         # print(widget)
#         # global selectedDate
#         # FocusOut event
#         if event.type() == QEvent.FocusOut:# and widget == window.textBrowserDBTitle:
#             print('Save entry?')
#             #     if QMessageBox.question(widget,
#             #              "Save journal entry?", " ",
#             #              QMessageBox.Save, QMessageBox.Cancel)\
#             #             == QMessageBox.Save:
#             #         addEntry(selectedDate, widget.toPlainText())
#             # addEntry(d, self.textBrowserJournalEntry.toPlainText())
#             # return False so that the widget will also handle the event
#             # otherwise it won't focus out
#         #     return False
#         # else:
#         #     we don't care about other events
#         return False
def getFile():
    fileDialog = QFileDialog()#
    fileDialog.setDirectory(G.workingDirectory)
    fileName = fileDialog.getOpenFileName(None,
                            'Open sesame', '', 'Journal database files (*.db)')
    # print(fileName[0])
    return fileName

def setWDir():
    fileDialog = QFileDialog()  #
    fileDialog.setDirectory(G.workingDirectory)
    fileName = fileDialog.getExistingDirectory(None,
                                          'Set working directory', '')
    # print(os.path)
    return fileName

def saveFile():
    fileDialog = QFileDialog()  #
    fileDialog.setDirectory(G.workingDirectory)
    fileName = fileDialog.getOpenFileName(None,
                                          'Create file for journal', '',
                                          'Journal database files (*.db)')
    # print(os.path)
    # print(fileName[0])
    return fileName