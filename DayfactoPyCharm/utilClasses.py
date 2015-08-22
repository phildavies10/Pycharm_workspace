from datetime import date, datetime
from PyQt5 import QtGui
from dateutil.parser import parse

__author__ = 'phil'
from PyQt5.QtWidgets import QInputDialog
import configparser

class CustomInputDialog(QInputDialog):
    def __init__(self, posx, posy, label, title, value, parent=None):
        QInputDialog.__init__(self)
        xoff = parent.pos().x()
        yoff = parent.pos().y()
        self.setGeometry(posx+xoff, posy+yoff, 300, 200)
        self.setLabelText(label)
        self.setWindowTitle(title)
        self.setTextValue(value)
        dlgFont = self.font()
        dlgFont.setPointSize(14)
        self.setFont(dlgFont)

class Entry():
    def __init__(self, entry_date, journal_entry, events_list):
        self.entry_date = entry_date
        self.journal_entry = journal_entry
        self.events_list = events_list
    def entryDate(self):
        return self.entry_date
    def journalEntry(self):
        return self.journal_entry
    def eventsList(self):
        return self.events_list

class Glob():
    entryText = ''
    eventText = ''
    # searchCase = False
    searchEventsCase = False
    searchEntriesCase = False
    journalStartDate = parse('2000-1-1')
    journalEndDate = parse('2018-12-31')
    fDateEntries = journalStartDate
    tDateEntries = journalEndDate
    fDateEvents = journalStartDate
    tDateEvents = journalEndDate
    entriesList = []
    eventsList = []
    categoryList = []
    periods = ['One off', 'Daily', 'Weekly', 'Monthly', 'Yearly']
    selectionColor = "#ED6511"
    dayNumberColor = "#1441A2"
    dayNumberBkgnd = '#E9F0F8'
    monthStyle = "color:blue; vertical-align:top; padding-left:20"
    daysListFlag = False
    categorySet = set()
    font = QtGui.QFont()
    font.setPointSize(11)
    entriesFont = font
    remindersPeriod = 1

    loadLast = False
    enableReminders = False
    workingDirectory = 'D:\\Documents\\Diaries\\DFPython'
    lastFile = 'D:\\Documents\\Diaries\\DFPython\\Dayfacto_2_ to 15-05-2015.db'

def configWrite(self, f='dfConfig.cfg'):
    config = configparser.ConfigParser()

    config['DEFAULT'] = {'LoadLast': 'no',
                         'EnableReminders': 'yes',
                         'WorkingDirectory': 'D:\\Documents\\Diaries\\DFPython'}
    if Glob.loadLast:
        val1 = 'yes'
    else:
        val1 = 'no'
    if Glob.enableReminders:
        val2 = 'yes'
    else:
        val2 = 'no'
    if Glob.daysListFlag:
        val3 = 'yes'
    else:
        val3 = 'no'
    config['dayfacto'] = {'LoadLast': val1,
                          'EnableReminders': val2,
                          'WorkingDirectory': Glob.workingDirectory,
                          'LastFile': Glob.lastFile,
                          'DaysListFlag': val3
                          }
    with open(f, 'w') as configfile:
        config.write(configfile)

def configRead(self, f='dfConfig.cfg'):
    config = configparser.ConfigParser()
    config.read(f)
    Glob.lastFile = config['dayfacto']['LastFile']
    Glob.loadLast = config['dayfacto'].getboolean('LoadLast')
    Glob.daysListFlag = config['dayfacto'].getboolean('DaysListFlag')
