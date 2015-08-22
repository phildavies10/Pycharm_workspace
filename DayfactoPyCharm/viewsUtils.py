'''
Created on 22 Mar 2015

@author: phil
'''
import operator
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextDocument, QTextOption
from PyQt5.QtWidgets import QStyledItemDelegate, QApplication, QStyle
from utilClasses import Glob as G

class WeekViewDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self)
    def paint(self, painter, option, index):
        text = index.model().data(index, Qt.DisplayRole)
        palette = QApplication.palette()
        document = QTextDocument()
        # if option.state & QStyle.State_Selected:
        #     document.setHtml("<p <center <font color={}>{}</font></center></p>".format(
        #         palette.highlightedText().color().name(), text))
        # else:
        document.setPlainText(text)
        if index.column() == 1:
            document.setTextWidth(350)
        elif index.column() == 2:
            document.setTextWidth(150)
        to = QTextOption()
        painter.save()
        painter.translate(option.rect.x(), option.rect.y())
        document.drawContents(painter)
        painter.restore()

class MonthViewDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self)

    def paint(self, painter, option, index):
        text = index.model().data(index, Qt.DisplayRole)
        document = QTextDocument()
        column = index.column()
        row = index.row()
        document.setTextWidth(115)
        if row % 2 == 0:
            document.setHtml(
                "<p style=margin-left:0; style=background-color:{}; style="
                "color:{}><center <b <font size={} >{}</font>"
                "</b></center></p>".format(G.dayNumberBkgnd,
                                           G.dayNumberColor, "3", text))
        elif option.state & QStyle.State_Selected:
            document.setHtml("<b> <font size={} font color={}>{}"
                             "</font></b>".format("3", G.selectionColor, text))

        else:
            document.setHtml(text)
        painter.save()
        painter.translate(option.rect.x(), option.rect.y())
        document.drawContents(painter)
        painter.restore()

class MonthViewTableModel(QAbstractTableModel):
    def __init__(self, datain, header='', parent=None):
        QAbstractTableModel.__init__(self)
        self.listdata = datain
        self.daysList = []
        self.header = header

    def data(self, index, value, role=Qt.DisplayRole):
        self.beginResetModel()
        if index.isValid():
            self.beginResetModel()
            column = index.column()
            row = index.row()
            if row%2 != 0:
                return self.listdata[column + 7*(int(row/2))]
            else:
                return self.daysList[column + 7 *(int(row / 2))]
            self.dataChanged.emit(index)  # ??
        else:
            return None

    def setAllData(self, newdata, daysList, monthDates):
        """ replace all data with new data """
        self.listdata = newdata
        self.daysList = daysList
        self.monthDates = monthDates
        self.beginResetModel()
        self.endResetModel()

    def flags(self, index):
        if not index.isValid():
            return None
        elif index.row()% 2 == 0:
            return Qt.NoItemFlags
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled #| Qt.CheckStateRole

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def rowCount(self, index=QModelIndex()):
        return 10

    def columnCount(self, index=QModelIndex()):
        return 7

class WeekViewTableModel(QAbstractTableModel):
    def __init__(self, datain, header='', parent=None):
        QAbstractTableModel.__init__(self)
        self.listdata = datain
        self.header = header

    def data(self, index, value, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        elif index.isValid() and 0 <= index.row() < len(self.listdata):
            self.beginResetModel()
            column = index.column()
            if column == 0:
                return self.listdata[index.row()][0]
            elif column == 1:
                return self.listdata[index.row()][1]
            elif column == 2:
                return self.listdata[index.row()][2]
            self.dataChanged.emit(index)  # ??
            return None
        return None

    def setAllData(self, newdata):
        """ replace all data with new data """
        self.listdata = newdata
        self.beginResetModel()
        self.endResetModel()

    def flags(self, index):
        if not index.isValid():
            return None
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled  # | Qt.CheckStateRole

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def rowCount(self, index=QModelIndex()):
        return len(self.listdata)

    def columnCount(self, index=QModelIndex()):
            return 3

class EventsViewTableModel(QAbstractTableModel):
    def __init__(self, datain, header='', parent=None):
        QAbstractTableModel.__init__(self)
        self.listdata = datain
        self.header = header

    def data(self, index, value, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        elif index.isValid() and 0 <= index.row() < len(self.listdata):
            self.beginResetModel()
            column = index.column()
            row = index.row()
            # self.endResetModel()
            # self.dataChanged.emit(index)  # ??
            return self.listdata[row][column]
        return None

    def setAllData(self, newdata):
        """ replace all data with new data """
        self.beginResetModel()
        self.listdata = newdata
        self.endResetModel()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        if Ncol == 2:
            Ncol = 8
        self.layoutAboutToBeChanged.emit()
        self.listdata = sorted(self.listdata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.listdata.reverse()
        self.layoutChanged.emit()

    def flags(self, index):
        if not index.isValid():
            return None
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled  # | Qt.CheckStateRole

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def rowCount(self, index=QModelIndex()):
        return len(self.listdata)

    def columnCount(self, index=QModelIndex()):
            return 9

class EntriesViewDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self)

    def paint(self, painter, option, index):
        text = index.model().data(index, Qt.DisplayRole)
        document = QTextDocument()
        # metrics = QFontMetrics(document.defaultFont())
        metrics = painter.fontMetrics()
        # font = QFont()
        # font.setPointSize(12)
        document.setDefaultFont(G.entriesFont)
        if index.column() == 0:
            document.setTextWidth(69)
        elif index.column() == 1:
            document.setTextWidth(514)
        if option.state & QStyle.State_Selected:
            document.setHtml("<b bgcolor=#E6E600> <font size={} font color={}>{}"
                             "</font></b>".format("2", G.selectionColor, text))
        else:
            w = metrics.boundingRect('W').width()

            # print(w)
            txt = text[0:(514*4)//w]
            document.setHtml("<p align (center) bgcolor=white> <font size={} "
                             "font color={}>{}"
                             "</font></p>".format("2", "black", txt))
        painter.save()
        painter.translate(option.rect.x(), option.rect.y())
        document.drawContents(painter)
        painter.restore()
        # w = metrics.boundingRect('W').width()
        # print('W = ',w) - 11 pixels

class RemindersTableDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self)

    def paint(self, painter, option, index):
        text = index.model().data(index, Qt.DisplayRole)
        palette = QApplication.palette()
        document = QTextDocument()
        if option.state & QStyle.State_Selected:
            document.setHtml("<p <center <font size={} font color={}>{}"
                             "</font></center></p>".format(
                "5", palette.highlightedText().color().name(), text))
        else:
            document.setPlainText(text)
        # if index.column() == 1:
        #     document.setTextWidth(350)
        # elif index.column() == 2:
        #     document.setTextWidth(150)
        painter.save()
        painter.translate(option.rect.x(), option.rect.y())
        document.drawContents(painter)
        painter.restore()

class RemindersTableModel(QAbstractTableModel):
    def __init__(self, datain, header='', parent=None):
        QAbstractTableModel.__init__(self)
        self.listdata = datain
        self.header = header

    def data(self, index, value, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        elif index.isValid() and 0 <= index.row() < len(self.listdata):
            self.beginResetModel()
            column = index.column()
            if column == 0:
                return self.listdata[index.row()][0]
            elif column == 1:
                return self.listdata[index.row()][1]
            self.dataChanged.emit(index)  # ??
            return None
        return None

    def setAllData(self, newdata):
        """ replace all data with new data """
        self.beginResetModel()
        self.listdata = newdata
        self.endResetModel()

    def flags(self, index):
        if not index.isValid():
            return None
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled  # | Qt.CheckStateRole

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def rowCount(self, index=QModelIndex()):
        return len(self.listdata)

    def columnCount(self, index=QModelIndex()):
        return 2

class AlertsTableDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self)

    def paint(self, painter, option, index):
        text = index.model().data(index, Qt.DisplayRole)
        palette = QApplication.palette()
        document = QTextDocument()
        if option.state & QStyle.State_Selected:
            document.setHtml("<p <center <font size={} font color={}>{}"
                             "</font></center></p>".format(
                "5", palette.highlightedText().color().name(), text))
        else:
            document.setPlainText(text)
        painter.save()
        painter.translate(option.rect.x(), option.rect.y())
        document.drawContents(painter)
        painter.restore()

class AlertsTableModel(QAbstractTableModel):
    def __init__(self, datain, header='', parent=None):
        QAbstractTableModel.__init__(self)
        self.listdata = datain
        self.header = header

    def data(self, index, value, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        elif index.isValid() and 0 <= index.row() < len(self.listdata):
            self.beginResetModel()
            column = index.column()
            if column == 0:
                return self.listdata[index.row()][0]
            elif column == 1:
                return self.listdata[index.row()][1]
            self.dataChanged.emit(index)  # ??
            return None
        return None

    def setAllData(self, newdata):
        """ replace all data with new data """
        self.listdata = newdata
        self.beginResetModel()
        self.endResetModel()

    def flags(self, index):
        if not index.isValid():
            return None
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled  # | Qt.CheckStateRole

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def rowCount(self, index=QModelIndex()):
        return len(self.listdata)

    def columnCount(self, index=QModelIndex()):
        return 2

class EntriesViewTableModel(QAbstractTableModel):
    def __init__(self, datain, header='', parent=None):
        QAbstractTableModel.__init__(self)
        self.listdata = datain
        self.header = header

    def data(self, index, value, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        elif index.isValid() and 0 <= index.row() < len(self.listdata):
            self.beginResetModel()
            column = index.column()
            if column == 0:
                return self.listdata[index.row()][0]
            elif column == 1:
                return self.listdata[index.row()][1]
            elif column == 2:
                return self.listdata[index.row()][2]
            self.dataChanged.emit(index)  # ??
            return None
        return None

    def setAllData(self, newdata):
        """ replace all data with new data """
        self.listdata = newdata
        self.beginResetModel()
        self.endResetModel()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.layoutAboutToBeChanged.emit()
        if Ncol ==0:
            Ncol = 2
        self.listdata = sorted(self.listdata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.listdata.reverse()
        self.layoutChanged.emit()

    def flags(self, index):
        if not index.isValid():
            return None
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled  # | Qt.CheckStateRole

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def rowCount(self, index=QModelIndex()):
        return len(self.listdata)

    def columnCount(self, index=QModelIndex()):
        return 3

class EventsViewDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self)

    def paint(self, painter, option, index):
        text = index.model().data(index, Qt.DisplayRole)
        document = QTextDocument()
        if index.column() == 0:
            document.setTextWidth(160)
        elif index.column() == 1:
            document.setTextWidth(100)
        if option.state & QStyle.State_Selected:
            document.setHtml("<b style=background-color:{}> <font size={} font color={}>{}"
                             "</font></b>".format(G.dayNumberBkgnd, "3", G.selectionColor, text))
        else:
            document.setHtml(text)
        painter.save()
        painter.translate(option.rect.x(), option.rect.y())
        document.drawContents(painter)
        painter.restore()

class DaysListModel(QAbstractTableModel):
    def __init__(self, datain, header='', parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.listdata = sorted(datain)
        self.header = header

    def columnCount(self, parent=QModelIndex()):
        return 2

    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.listdata[index.row()][index.column()])
        else:
            return QVariant()

    def setAllData(self, newdata):
        """ replace all data with new data """
        self.listdata = newdata
        self.beginResetModel()
        self.endResetModel()

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    
    def sort(self, Ncol, order):
        self.layoutAboutToBeChanged.emit()
        self.arraydata = sorted(self.listdata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.layoutChanged.emit()

class EventsListModel(QAbstractListModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.listdata = datain

    def columnCount(self, parent=QModelIndex()):
        return 1

    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)

    def setAllData(self, newdata):
        """ replace all data with new data """
        self.listdata = newdata

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.listdata[index.row()])
        else:
            return QVariant()

    def setData(self, index):
        self.dataChanged.emit(index, index)
