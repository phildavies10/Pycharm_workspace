'''
Created on 24 Mar 2015

@author: phil
'''
from PyQt5 import QtGui
from PyQt5.QtWidgets import QAction

from genUtils import getFile

def connectSetup(self):
    self.textBrowserDBTitle.customContextMenuRequested.connect(self.editTitle)
    self.listViewEvents.currentItemChanged.connect(self.on_item_changed)
    self.listViewEvents.doubleClicked.connect(self.editEvent)
    self.tableViewWeekView.doubleClicked.connect(self.on_weekView_dblClicked)
    self.tableViewMonthView.doubleClicked.connect(self.on_monthView_dblClicked)
    self.tableViewEntries.doubleClicked.connect(self.on_tableViewEntries_dblClicked)
    self.tableViewEvents.doubleClicked.connect(self.on_tableViewEvents_dblClicked)
    self.daysTableView.clicked.connect(self.on_daysTableView_Clicked)
    self.toolButtonShowReminders.clicked.connect(self.showReminders)
    self.toolButtonOpenFile.clicked.connect(self.openFile)
    self.action_show_alerts.triggered.connect(self.showAlerts)
    self.action_import_icalendar.triggered.connect(self.importIcalendar)
    self.action_export_icalendar.triggered.connect(self.exportIcalendar)
    self.actionSave_config.triggered.connect(self.on_actionSave_config)
    self.actionOpen.triggered.connect(self.openFile)
    self.actionSet_working_directory.triggered.connect(self.setWDir)
    self.actionLoad_last.triggered.connect(self.toggleLoadLast)
    self.actionClose_current_journal.triggered.connect(self.clearCurrent)
    self.actionNew_journal.triggered.connect(self.newJournal)
    self.actionToggle_days_list.triggered.connect(self.toggleDaysList)
    self.actionCategory_manager.triggered.connect(self.categoryManager)
    self.actionNew_event.triggered.connect(self.on_toolButtonNewEvent_clicked)
    self.actionEdit_event.triggered.connect(self.editEvent)
    self.actionDay_view.triggered.connect(self.on_toolButtonDayView_clicked)
    self.actionWeek_view.triggered.connect(self.on_toolButtonWeekView_clicked)
    self.actionMonth_view.triggered.connect(self.on_toolButtonMonthView_clicked)
    self.actionEntries_view.triggered.connect(self.on_toolButtonEntries_clicked)
    self.actionEvents_view.triggered.connect(self.on_toolButtonEvents_clicked)
    self.actionEvents_view.triggered.connect(self.on_toolButtonEvents_clicked)
    self.actionCategories_view.triggered.connect(self.on_toolButtonCategories_clicked)
    self.actionReminders_view.triggered.connect(self.showReminders)

def actionsSetup(self):
    fileNewAction = createAction(self, "&New", slot=getFile,
                        tip="Open a journal")
    editEventEventsAction = createAction(self, "&Edit", slot=
                        self.on_tableViewEvents_dblClicked, tip="Edit event")
    editEventMonthAction = createAction(self, "&Edit", slot=
                        self.editEvent, tip="Edit event")
    editEventAction = createAction(self, "&Edit", slot=
                        self.editEvent, tip="Edit event")
    deleteEventAction = createAction(self, "&Delete",
                        slot=self.deleteEventView, tip="Edit event")
    gotoEntryAction = createAction(self, "&Goto entry", slot=self.gotoEntry,
                        tip="Edit event")
    showAlertsAction = createAction(self, "&Alerts", slot=self.showAlerts,
                        tip="Activate alerts")
    self.toolButtonOpenFile.addAction(fileNewAction)
    self.tableViewEvents.addAction(editEventEventsAction)
    self.tableViewEvents.addAction(gotoEntryAction)
    self.tableViewMonthView.addAction(gotoEntryAction)
    self.tableViewMonthView.addAction(editEventMonthAction)
    self.tableViewEvents.addAction(deleteEventAction)
    self.listViewEvents.addAction(deleteEventAction)
    self.listViewEvents.addAction(editEventAction)

def createAction(self, text, slot=None, shortcut=None, icon=None,
                 tip=None, checkable=False, signal="triggered"):
    action = QAction(text, self)
    if icon is not None:
        action.setIcon(QtGui.QIcon(":/{}.png".format(icon)))
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if slot is not None:
        getattr(action, signal).connect(slot) #old-style: self.connect(action, SIGNAL(signal), slot)
    if checkable:
        action.setCheckable(True)
    return action
        
