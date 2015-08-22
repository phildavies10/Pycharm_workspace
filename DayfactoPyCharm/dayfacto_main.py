# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayfacto_main_stack.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 766)
        MainWindow.setSizeIncrement(QtCore.QSize(2, 2))
        MainWindow.setBaseSize(QtCore.QSize(200, 200))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(90, 120, 110, 22))
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.calendarSelectDate = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarSelectDate.setGeometry(QtCore.QRect(15, 150, 221, 191))
        self.calendarSelectDate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calendarSelectDate.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarSelectDate.setDateEditEnabled(True)
        self.calendarSelectDate.setObjectName("calendarSelectDate")
        self.groupBoxToolBar = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxToolBar.setGeometry(QtCore.QRect(10, 5, 891, 31))
        self.groupBoxToolBar.setTitle("")
        self.groupBoxToolBar.setObjectName("groupBoxToolBar")
        self.toolButtonOpenFile = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonOpenFile.setGeometry(QtCore.QRect(5, 10, 56, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonOpenFile.setFont(font)
        self.toolButtonOpenFile.setObjectName("toolButtonOpenFile")
        self.toolButtonNewEvent = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonNewEvent.setGeometry(QtCore.QRect(585, 10, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonNewEvent.setFont(font)
        self.toolButtonNewEvent.setObjectName("toolButtonNewEvent")
        self.toolButtonPurge = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonPurge.setGeometry(QtCore.QRect(660, 10, 81, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonPurge.setFont(font)
        self.toolButtonPurge.setObjectName("toolButtonPurge")
        self.toolButtonWeekView = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonWeekView.setGeometry(QtCore.QRect(140, 10, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonWeekView.setFont(font)
        self.toolButtonWeekView.setObjectName("toolButtonWeekView")
        self.toolButtonDayView = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonDayView.setGeometry(QtCore.QRect(75, 10, 61, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonDayView.setFont(font)
        self.toolButtonDayView.setObjectName("toolButtonDayView")
        self.toolButtonMonthView = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonMonthView.setGeometry(QtCore.QRect(215, 10, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonMonthView.setFont(font)
        self.toolButtonMonthView.setObjectName("toolButtonMonthView")
        self.toolButtonEntries = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonEntries.setGeometry(QtCore.QRect(290, 10, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonEntries.setFont(font)
        self.toolButtonEntries.setObjectName("toolButtonEntries")
        self.toolButtonEvents = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonEvents.setGeometry(QtCore.QRect(345, 10, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonEvents.setFont(font)
        self.toolButtonEvents.setObjectName("toolButtonEvents")
        self.toolButtonCategories = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonCategories.setGeometry(QtCore.QRect(400, 10, 66, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonCategories.setFont(font)
        self.toolButtonCategories.setObjectName("toolButtonCategories")
        self.toolButtonShowReminders = QtWidgets.QToolButton(self.groupBoxToolBar)
        self.toolButtonShowReminders.setGeometry(QtCore.QRect(470, 10, 96, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButtonShowReminders.setFont(font)
        self.toolButtonShowReminders.setObjectName("toolButtonShowReminders")
        self.labelSelectedDate = QtWidgets.QLabel(self.centralwidget)
        self.labelSelectedDate.setGeometry(QtCore.QRect(375, 45, 371, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.labelSelectedDate.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.labelSelectedDate.setFont(font)
        self.labelSelectedDate.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelSelectedDate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelSelectedDate.setTextFormat(QtCore.Qt.AutoText)
        self.labelSelectedDate.setContentsMargins(7, 7, 7, 7)
        self.labelSelectedDate.setObjectName("labelSelectedDate")
        self.textBrowserDBTitle = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserDBTitle.setGeometry(QtCore.QRect(15, 50, 301, 36))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(12)
        self.textBrowserDBTitle.setFont(font)
        self.textBrowserDBTitle.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textBrowserDBTitle.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textBrowserDBTitle.setUndoRedoEnabled(True)
        self.textBrowserDBTitle.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowserDBTitle.setReadOnly(True)
        self.textBrowserDBTitle.setAcceptRichText(False)
        self.textBrowserDBTitle.setObjectName("textBrowserDBTitle")
        self.frameDates = QtWidgets.QFrame(self.centralwidget)
        self.frameDates.setGeometry(QtCore.QRect(15, 360, 116, 146))
        self.frameDates.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDates.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameDates.setObjectName("frameDates")
        self.pushButtonToday = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonToday.setGeometry(QtCore.QRect(30, 10, 51, 23))
        self.pushButtonToday.setObjectName("pushButtonToday")
        self.labelWeek = QtWidgets.QLabel(self.frameDates)
        self.labelWeek.setGeometry(QtCore.QRect(10, 70, 31, 16))
        self.labelWeek.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelWeek.setObjectName("labelWeek")
        self.pushButtonFwdMonth = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonFwdMonth.setGeometry(QtCore.QRect(75, 90, 26, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButtonFwdMonth.setFont(font)
        self.pushButtonFwdMonth.setAutoRepeat(True)
        self.pushButtonFwdMonth.setObjectName("pushButtonFwdMonth")
        self.pushButtonBackMonth = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonBackMonth.setGeometry(QtCore.QRect(45, 90, 26, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButtonBackMonth.setFont(font)
        self.pushButtonBackMonth.setAutoRepeat(True)
        self.pushButtonBackMonth.setObjectName("pushButtonBackMonth")
        self.pushButtonFwdWeek = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonFwdWeek.setGeometry(QtCore.QRect(75, 65, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButtonFwdWeek.setFont(font)
        self.pushButtonFwdWeek.setAutoRepeat(True)
        self.pushButtonFwdWeek.setObjectName("pushButtonFwdWeek")
        self.labelWeek_2 = QtWidgets.QLabel(self.frameDates)
        self.labelWeek_2.setGeometry(QtCore.QRect(10, 95, 31, 16))
        self.labelWeek_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelWeek_2.setObjectName("labelWeek_2")
        self.pushButtonBackYear = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonBackYear.setGeometry(QtCore.QRect(40, 115, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButtonBackYear.setFont(font)
        self.pushButtonBackYear.setAutoRepeat(True)
        self.pushButtonBackYear.setObjectName("pushButtonBackYear")
        self.labelDay = QtWidgets.QLabel(self.frameDates)
        self.labelDay.setGeometry(QtCore.QRect(10, 45, 26, 16))
        self.labelDay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelDay.setObjectName("labelDay")
        self.pushButtonBackDay = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonBackDay.setGeometry(QtCore.QRect(55, 40, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButtonBackDay.setFont(font)
        self.pushButtonBackDay.setAutoRepeat(True)
        self.pushButtonBackDay.setObjectName("pushButtonBackDay")
        self.pushButtonFwdDay = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonFwdDay.setGeometry(QtCore.QRect(75, 40, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButtonFwdDay.setFont(font)
        self.pushButtonFwdDay.setAutoRepeat(True)
        self.pushButtonFwdDay.setObjectName("pushButtonFwdDay")
        self.pushButtonBackWeek = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonBackWeek.setGeometry(QtCore.QRect(50, 65, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButtonBackWeek.setFont(font)
        self.pushButtonBackWeek.setAutoRepeat(True)
        self.pushButtonBackWeek.setObjectName("pushButtonBackWeek")
        self.pushButtonFwdYear = QtWidgets.QPushButton(self.frameDates)
        self.pushButtonFwdYear.setGeometry(QtCore.QRect(75, 115, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButtonFwdYear.setFont(font)
        self.pushButtonFwdYear.setAutoRepeat(True)
        self.pushButtonFwdYear.setObjectName("pushButtonFwdYear")
        self.labelYear = QtWidgets.QLabel(self.frameDates)
        self.labelYear.setGeometry(QtCore.QRect(10, 120, 21, 16))
        self.labelYear.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelYear.setObjectName("labelYear")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(250, 100, 621, 611))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.stackedWidget.setAutoFillBackground(True)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setObjectName("stackedWidget")
        self.dayView = QtWidgets.QWidget()
        self.dayView.setObjectName("dayView")
        self.pushButtonClearEntry = QtWidgets.QPushButton(self.dayView)
        self.pushButtonClearEntry.setGeometry(QtCore.QRect(510, 10, 75, 23))
        self.pushButtonClearEntry.setObjectName("pushButtonClearEntry")
        self.pushButtonSaveEntry = QtWidgets.QPushButton(self.dayView)
        self.pushButtonSaveEntry.setGeometry(QtCore.QRect(425, 10, 75, 23))
        self.pushButtonSaveEntry.setObjectName("pushButtonSaveEntry")
        self.frameEvents = QtWidgets.QFrame(self.dayView)
        self.frameEvents.setGeometry(QtCore.QRect(15, 440, 571, 166))
        self.frameEvents.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameEvents.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameEvents.setLineWidth(1)
        self.frameEvents.setMidLineWidth(0)
        self.frameEvents.setObjectName("frameEvents")
        self.listViewEvents = QtWidgets.QListWidget(self.frameEvents)
        self.listViewEvents.setGeometry(QtCore.QRect(10, 10, 231, 146))
        self.listViewEvents.setModelColumn(0)
        self.listViewEvents.setWordWrap(True)
        self.listViewEvents.setObjectName("listViewEvents")
        self.labelCategory = QtWidgets.QLabel(self.frameEvents)
        self.labelCategory.setGeometry(QtCore.QRect(255, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategory.setFont(font)
        self.labelCategory.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelCategory.setObjectName("labelCategory")
        self.labelReminder = QtWidgets.QLabel(self.frameEvents)
        self.labelReminder.setGeometry(QtCore.QRect(480, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelReminder.setFont(font)
        self.labelReminder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelReminder.setObjectName("labelReminder")
        self.textBrowserReminder = QtWidgets.QTextBrowser(self.frameEvents)
        self.textBrowserReminder.setGeometry(QtCore.QRect(480, 30, 81, 26))
        self.textBrowserReminder.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowserReminder.setObjectName("textBrowserReminder")
        self.labelNotes = QtWidgets.QLabel(self.frameEvents)
        self.labelNotes.setGeometry(QtCore.QRect(260, 65, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNotes.setFont(font)
        self.labelNotes.setObjectName("labelNotes")
        self.textBrowserNotes = QtWidgets.QTextBrowser(self.frameEvents)
        self.textBrowserNotes.setGeometry(QtCore.QRect(255, 85, 306, 71))
        self.textBrowserNotes.setObjectName("textBrowserNotes")
        self.textBrowserCategory = QtWidgets.QTextBrowser(self.frameEvents)
        self.textBrowserCategory.setGeometry(QtCore.QRect(255, 30, 216, 26))
        self.textBrowserCategory.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowserCategory.setObjectName("textBrowserCategory")
        self.textBrowserJournalEntry = QtWidgets.QTextBrowser(self.dayView)
        self.textBrowserJournalEntry.setGeometry(QtCore.QRect(265, 40, 321, 391))
        font = QtGui.QFont()
        font.setFamily("Square721 BT")
        font.setPointSize(12)
        self.textBrowserJournalEntry.setFont(font)
        self.textBrowserJournalEntry.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBrowserJournalEntry.setFrameShape(QtWidgets.QFrame.Panel)
        self.textBrowserJournalEntry.setLineWidth(2)
        self.textBrowserJournalEntry.setReadOnly(False)
        self.textBrowserJournalEntry.setObjectName("textBrowserJournalEntry")
        self.labelJournalEntry = QtWidgets.QLabel(self.dayView)
        self.labelJournalEntry.setGeometry(QtCore.QRect(265, 15, 116, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.labelJournalEntry.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Square721 BT")
        font.setPointSize(12)
        self.labelJournalEntry.setFont(font)
        self.labelJournalEntry.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelJournalEntry.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelJournalEntry.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelJournalEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.labelJournalEntry.setObjectName("labelJournalEntry")
        self.daysTableView = QtWidgets.QTableView(self.dayView)
        self.daysTableView.setGeometry(QtCore.QRect(15, 40, 241, 391))
        self.daysTableView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.daysTableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.daysTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.daysTableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.daysTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.daysTableView.setObjectName("daysTableView")
        self.stackedWidget.addWidget(self.dayView)
        self.weekView = QtWidgets.QWidget()
        self.weekView.setObjectName("weekView")
        self.tableViewWeekView = QtWidgets.QTableView(self.weekView)
        self.tableViewWeekView.setGeometry(QtCore.QRect(10, 36, 596, 566))
        self.tableViewWeekView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableViewWeekView.setAlternatingRowColors(True)
        self.tableViewWeekView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewWeekView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableViewWeekView.setCornerButtonEnabled(False)
        self.tableViewWeekView.setObjectName("tableViewWeekView")
        self.tableViewWeekView.horizontalHeader().setDefaultSectionSize(200)
        self.tableViewWeekView.horizontalHeader().setStretchLastSection(True)
        self.tableViewWeekView.verticalHeader().setDefaultSectionSize(72)
        self.labelWeekView = QtWidgets.QLabel(self.weekView)
        self.labelWeekView.setGeometry(QtCore.QRect(20, 10, 566, 21))
        self.labelWeekView.setObjectName("labelWeekView")
        self.stackedWidget.addWidget(self.weekView)
        self.monthView = QtWidgets.QWidget()
        self.monthView.setObjectName("monthView")
        self.tableViewMonthView = QtWidgets.QTableView(self.monthView)
        self.tableViewMonthView.setGeometry(QtCore.QRect(10, 40, 596, 561))
        self.tableViewMonthView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableViewMonthView.setSortingEnabled(True)
        self.tableViewMonthView.setObjectName("tableViewMonthView")
        self.tableViewMonthView.horizontalHeader().setStretchLastSection(True)
        self.tableViewMonthView.verticalHeader().setVisible(False)
        self.labelMonthView = QtWidgets.QLabel(self.monthView)
        self.labelMonthView.setGeometry(QtCore.QRect(10, 10, 566, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMonthView.setFont(font)
        self.labelMonthView.setAutoFillBackground(True)
        self.labelMonthView.setStyleSheet("color:red; vertical-align:top\n"
"")
        self.labelMonthView.setTextFormat(QtCore.Qt.RichText)
        self.labelMonthView.setObjectName("labelMonthView")
        self.stackedWidget.addWidget(self.monthView)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.tableViewEntries = QtWidgets.QTableView(self.page)
        self.tableViewEntries.setGeometry(QtCore.QRect(10, 41, 601, 561))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableViewEntries.setFont(font)
        self.tableViewEntries.setAlternatingRowColors(True)
        self.tableViewEntries.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewEntries.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableViewEntries.setObjectName("tableViewEntries")
        self.tableViewEntries.verticalHeader().setVisible(False)
        self.tableViewEntries.verticalHeader().setHighlightSections(False)
        self.pushButtonSearchEntries = QtWidgets.QPushButton(self.page)
        self.pushButtonSearchEntries.setGeometry(QtCore.QRect(10, 10, 81, 23))
        self.pushButtonSearchEntries.setObjectName("pushButtonSearchEntries")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableViewEvents = QtWidgets.QTableView(self.page_2)
        self.tableViewEvents.setGeometry(QtCore.QRect(10, 41, 601, 561))
        self.tableViewEvents.setAlternatingRowColors(False)
        self.tableViewEvents.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewEvents.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableViewEvents.setSortingEnabled(True)
        self.tableViewEvents.setObjectName("tableViewEvents")
        self.tableViewEvents.verticalHeader().setVisible(False)
        self.pushButtonSearchEvents = QtWidgets.QPushButton(self.page_2)
        self.pushButtonSearchEvents.setGeometry(QtCore.QRect(10, 10, 81, 23))
        self.pushButtonSearchEvents.setObjectName("pushButtonSearchEvents")
        self.stackedWidget.addWidget(self.page_2)
        self.frameDates.raise_()
        self.dateEdit.raise_()
        self.calendarSelectDate.raise_()
        self.groupBoxToolBar.raise_()
        self.labelSelectedDate.raise_()
        self.textBrowserDBTitle.raise_()
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuViews = QtWidgets.QMenu(self.menubar)
        self.menuViews.setObjectName("menuViews")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSet_working_directory = QtWidgets.QAction(MainWindow)
        self.actionSet_working_directory.setObjectName("actionSet_working_directory")
        self.actionSave_config = QtWidgets.QAction(MainWindow)
        self.actionSave_config.setObjectName("actionSave_config")
        self.actionLoad_last = QtWidgets.QAction(MainWindow)
        self.actionLoad_last.setCheckable(True)
        self.actionLoad_last.setObjectName("actionLoad_last")
        self.actionNew_journal = QtWidgets.QAction(MainWindow)
        self.actionNew_journal.setObjectName("actionNew_journal")
        self.actionClose_current_journal = QtWidgets.QAction(MainWindow)
        self.actionClose_current_journal.setObjectName("actionClose_current_journal")
        self.actionToggle_days_list = QtWidgets.QAction(MainWindow)
        self.actionToggle_days_list.setObjectName("actionToggle_days_list")
        self.actionCategory_manager = QtWidgets.QAction(MainWindow)
        self.actionCategory_manager.setObjectName("actionCategory_manager")
        self.action_show_alerts = QtWidgets.QAction(MainWindow)
        self.action_show_alerts.setObjectName("action_show_alerts")
        self.action_import_icalendar = QtWidgets.QAction(MainWindow)
        self.action_import_icalendar.setObjectName("action_import_icalendar")
        self.action_export_icalendar = QtWidgets.QAction(MainWindow)
        self.action_export_icalendar.setObjectName("action_export_icalendar")
        self.actionDay_view = QtWidgets.QAction(MainWindow)
        self.actionDay_view.setObjectName("actionDay_view")
        self.actionWeek_view = QtWidgets.QAction(MainWindow)
        self.actionWeek_view.setObjectName("actionWeek_view")
        self.actionMonth_view = QtWidgets.QAction(MainWindow)
        self.actionMonth_view.setObjectName("actionMonth_view")
        self.actionEntries_view = QtWidgets.QAction(MainWindow)
        self.actionEntries_view.setObjectName("actionEntries_view")
        self.actionEvents_view = QtWidgets.QAction(MainWindow)
        self.actionEvents_view.setObjectName("actionEvents_view")
        self.actionCategories_view = QtWidgets.QAction(MainWindow)
        self.actionCategories_view.setObjectName("actionCategories_view")
        self.actionReminders_view = QtWidgets.QAction(MainWindow)
        self.actionReminders_view.setObjectName("actionReminders_view")
        self.actionNew_event = QtWidgets.QAction(MainWindow)
        self.actionNew_event.setObjectName("actionNew_event")
        self.actionEdit_event = QtWidgets.QAction(MainWindow)
        self.actionEdit_event.setObjectName("actionEdit_event")
        self.actionDelete_event = QtWidgets.QAction(MainWindow)
        self.actionDelete_event.setObjectName("actionDelete_event")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionNew_journal)
        self.menuFile.addAction(self.actionClose_current_journal)
        self.menuOptions.addAction(self.actionSet_working_directory)
        self.menuOptions.addAction(self.actionSave_config)
        self.menuOptions.addAction(self.actionLoad_last)
        self.menuOptions.addAction(self.actionToggle_days_list)
        self.menuOptions.addAction(self.actionCategory_manager)
        self.menuOptions.addAction(self.action_show_alerts)
        self.menuOptions.addAction(self.action_import_icalendar)
        self.menuOptions.addAction(self.action_export_icalendar)
        self.menuViews.addAction(self.actionDay_view)
        self.menuViews.addAction(self.actionWeek_view)
        self.menuViews.addAction(self.actionMonth_view)
        self.menuViews.addAction(self.actionEntries_view)
        self.menuViews.addAction(self.actionEvents_view)
        self.menuViews.addAction(self.actionCategories_view)
        self.menuViews.addAction(self.actionReminders_view)
        self.menuEdit.addAction(self.actionNew_event)
        self.menuEdit.addAction(self.actionEdit_event)
        self.menuEdit.addAction(self.actionDelete_event)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuViews.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.labelWeek.setBuddy(self.pushButtonBackMonth)
        self.labelWeek_2.setBuddy(self.pushButtonBackMonth)
        self.labelDay.setBuddy(self.pushButtonBackDay)
        self.labelYear.setBuddy(self.pushButtonBackYear)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.dateEdit.dateChanged['QDate'].connect(self.calendarSelectDate.setSelectedDate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textBrowserJournalEntry, self.pushButtonToday)
        MainWindow.setTabOrder(self.pushButtonToday, self.pushButtonBackDay)
        MainWindow.setTabOrder(self.pushButtonBackDay, self.pushButtonFwdDay)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dayfacto"))
        self.toolButtonOpenFile.setText(_translate("MainWindow", "Open file"))
        self.toolButtonNewEvent.setText(_translate("MainWindow", "New event"))
        self.toolButtonPurge.setText(_translate("MainWindow", "Purge entries"))
        self.toolButtonWeekView.setText(_translate("MainWindow", "Week view"))
        self.toolButtonDayView.setText(_translate("MainWindow", "Day view"))
        self.toolButtonMonthView.setText(_translate("MainWindow", "Month view"))
        self.toolButtonEntries.setText(_translate("MainWindow", "Entries"))
        self.toolButtonEvents.setText(_translate("MainWindow", "Events"))
        self.toolButtonCategories.setText(_translate("MainWindow", "Categories"))
        self.toolButtonShowReminders.setText(_translate("MainWindow", "ShowReminders"))
        self.labelSelectedDate.setText(_translate("MainWindow", "Selected date"))
        self.textBrowserDBTitle.setToolTip(_translate("MainWindow", "Right click to edit"))
        self.textBrowserDBTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Liberation Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00aa00;\">Journal title</span></p></body></html>"))
        self.pushButtonToday.setText(_translate("MainWindow", "Today"))
        self.labelWeek.setText(_translate("MainWindow", "Week"))
        self.pushButtonFwdMonth.setText(_translate("MainWindow", ">>>"))
        self.pushButtonBackMonth.setText(_translate("MainWindow", "<<<"))
        self.pushButtonFwdWeek.setText(_translate("MainWindow", ">>"))
        self.labelWeek_2.setText(_translate("MainWindow", "Month"))
        self.pushButtonBackYear.setText(_translate("MainWindow", "<<<<"))
        self.labelDay.setText(_translate("MainWindow", "Day"))
        self.pushButtonBackDay.setText(_translate("MainWindow", "<"))
        self.pushButtonFwdDay.setText(_translate("MainWindow", ">"))
        self.pushButtonBackWeek.setText(_translate("MainWindow", "<<"))
        self.pushButtonFwdYear.setText(_translate("MainWindow", ">>>>"))
        self.labelYear.setText(_translate("MainWindow", "Year"))
        self.pushButtonClearEntry.setText(_translate("MainWindow", "Clear entry"))
        self.pushButtonSaveEntry.setText(_translate("MainWindow", "Save entry"))
        self.labelCategory.setText(_translate("MainWindow", "Category"))
        self.labelReminder.setText(_translate("MainWindow", "Reminder"))
        self.labelNotes.setText(_translate("MainWindow", "Notes"))
        self.textBrowserJournalEntry.setToolTip(_translate("MainWindow", "Type and edit journal entry"))
        self.labelJournalEntry.setText(_translate("MainWindow", "Journal entry"))
        self.labelWeekView.setText(_translate("MainWindow", "Week No. start date - end date"))
        self.labelMonthView.setText(_translate("MainWindow", "Month"))
        self.pushButtonSearchEntries.setText(_translate("MainWindow", "Search entries"))
        self.pushButtonSearchEvents.setText(_translate("MainWindow", "Search events"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuViews.setTitle(_translate("MainWindow", "Views"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSet_working_directory.setText(_translate("MainWindow", "Set working directory"))
        self.actionSave_config.setText(_translate("MainWindow", "Save config"))
        self.actionLoad_last.setText(_translate("MainWindow", "Load last journal on start"))
        self.actionNew_journal.setText(_translate("MainWindow", "New journal"))
        self.actionClose_current_journal.setText(_translate("MainWindow", "Close current journal"))
        self.actionToggle_days_list.setText(_translate("MainWindow", "Toggle days list"))
        self.actionCategory_manager.setText(_translate("MainWindow", "Category manager"))
        self.action_show_alerts.setText(_translate("MainWindow", "Activate alerts"))
        self.action_import_icalendar.setText(_translate("MainWindow", "Import iCalendar"))
        self.action_export_icalendar.setText(_translate("MainWindow", "Export iCalendar"))
        self.actionDay_view.setText(_translate("MainWindow", "Day view"))
        self.actionWeek_view.setText(_translate("MainWindow", "Week view"))
        self.actionMonth_view.setText(_translate("MainWindow", "Month view"))
        self.actionEntries_view.setText(_translate("MainWindow", "Entries"))
        self.actionEvents_view.setText(_translate("MainWindow", "Events"))
        self.actionCategories_view.setText(_translate("MainWindow", "Categories"))
        self.actionReminders_view.setText(_translate("MainWindow", "Reminders"))
        self.actionNew_event.setText(_translate("MainWindow", "New event"))
        self.actionEdit_event.setText(_translate("MainWindow", "Edit event"))
        self.actionDelete_event.setText(_translate("MainWindow", "Delete event"))

