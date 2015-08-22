import sqlite3
from PyQt5.QtCore import QVariant
from dateutil.rrule import *
from dateutil.relativedelta import *
from datetime import *
from PyQt5.QtSql import *
import eventEditDialog
from utilClasses import Glob as G

ASCENDING = 0
DESCENDING = HORIZONTAL = 1
periodDic = {1: DAILY,
             2: WEEKLY,
             3: MONTHLY,
             4: YEARLY
             }

cur = conn = None
# global dbFile, cur, conn
dbFile = 'Dayfacto_2.db'

def dbInit(dbFile='Dayfacto_2.db'):
    global cur, conn
    if dbFile:
        conn = sqlite3.connect(dbFile, detect_types=sqlite3.PARSE_DECLTYPES
                          | sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        for cat in fetchCategories():
            eventEditDialog.G.categoryList.append(cat['name'])
        eventEditDialog.G.categoryList.sort()
        G.categorySet = set(G.categoryList)

eventData = {}

def weekViewInit(wDate):
    wStart = wDate - relativedelta(weekday=MO(-1))
    return list(rrule(DAILY, count=7, dtstart=wStart))

def monthViewInit(mDate):
    mDate.replace(day=1)
    mStart = mDate - relativedelta(day=1, weekday=MO(-1))
    return list(rrule(DAILY, count=35, dtstart=mStart))

def fetchCategories():
    global cur
    cur.execute("SELECT name, catType FROM categories ")
    return cur.fetchall()

def fetchEvent(rid=1):
    global cur
    conn.row_factory = sqlite3.Row
    cur.execute("SELECT * FROM diary_events WHERE EventNumber = ?", (rid,))
    return cur.fetchone()

def getEventTitles(dt):
    ent = fetchEntry(dt)
    evs = ''
    if ent is not None:
        if len(ent[1]) > 0:
            l = eval(ent[1])
            m = list(l)
            for n in m:
                e = fetchEvent(n)
                if e is not None:
                    if e[7] in G.categorySet:
                        evs += (e[5]) + '\n'
    return evs

def fetchEntry(r_date=date.today()):
    global cur
    try:
        cur.execute("SELECT journal_entry, event_list, entry_date FROM diary_entries "
        "WHERE entry_date = ?", (r_date,))
        d = cur.fetchone()
        # print('cur: ', d['journal_entry'])
        return d if d is not None else None
    except:
        return

def fetchAllEntries():
    global cur
    try:
        cur.execute("SELECT entry_date, journal_entry FROM diary_entries WHERE "
                    "journal_entry > '' ORDER BY entry_date")
        d = cur.fetchall()
        return d if d is not None else None
    except:
        return

def fetchAllEntriesNoBlanks():
    global cur
    try:
        cur.execute(
            "SELECT entry_date, journal_entry FROM diary_entries"
            " WHERE journal_entry != '' ORDER BY entry_date")
        d = cur.fetchall()
    except:
        d = None
    return d

def fetchAllEvents():
    global cur
    try:
        cur.execute(
            "SELECT Title, Category, StartDate, EndDate, Period, NoOfTimes,"
            " PeriodValue, DOB, EventNumber FROM diary_events"
            " ORDER BY StartDate")
        d = cur.fetchall()
    except:
        d = None
    return d

def fetchEventsByDates(fromDate, toDate, str, case=False):
    global cur
    fDate = fromDate.toPyDate()
    tDate = toDate.toPyDate()
    str = '%' + str + '%'
    if case:
        cur.execute("PRAGMA case_sensitive_like = 1")
    else:
        cur.execute("PRAGMA case_sensitive_like = 0")
    try:
        cur.execute(
            "SELECT Title, Category, StartDate, EndDate, Period, NoOfTimes,"
            " PeriodValue, DOB, EventNumber  FROM diary_events"
            " WHERE StartDate BETWEEN ? AND ?  AND Title LIKE ? ", (fDate, tDate, str))
        d = cur.fetchall()
        return d if d is not None else None
    except:
        return

def fetchAlerts(fromDate):
    global cur
    fDate = fromDate  # .toPyDate()
    tDate = fDate + relativedelta(months=+1)
    # try:
    cur.execute(
        "SELECT event_list, entry_date FROM diary_entries"
        " WHERE entry_date BETWEEN ? AND ? ",
        (fDate, tDate))
    d = cur.fetchall()
    # except:
    evs = []
    for ev in d:
        if len(ev[0]) > 0:
            l = eval(ev[0])
            m = list(l)
            for n in m:
                e = fetchEvent(n)
                if e is not None:
                    if (e[11] is not None):
                        if (ev[1] - fDate).days <= e[11]:
                            evs.append(((e[5]), (ev[1].strftime(
                                "%a  %d/%m/%Y"))))
    return evs


def fetchReminders(fromDate, toDate):
    global cur
    fDate = fromDate#.toPyDate()
    tDate = toDate#.toPyDate()
    try:
        cur.execute(
            "SELECT event_list, entry_date FROM diary_entries"
            " WHERE entry_date BETWEEN ? AND ? ",
            (fDate, tDate))
        d = cur.fetchall()
    # return d if d is not None else None
    except: ...
    evs = []
    t =''
    for ev in d:
        if len(ev[0]) > 0:
            l = eval(ev[0])
            m = list(l)
            for n in m:
                e = fetchEvent(n)
                if e is not None:
                    # t += '{:<30}'.format(e[5])# + str(e[1]))
                    evs.append(((e[5]), (ev[1].strftime(
                        "%a  %d/%m/%Y"))))
                    # evs.append((e[5].ljust(30) + str(e[1]).rjust(9)))
    return evs

def fetchEntriesByDates(fromDate, toDate, str, case=False):
    global cur
    fDate = fromDate.toPyDate()
    tDate = toDate.toPyDate()
    str = '%' + str + '%'
    if case:
        cur.execute("PRAGMA case_sensitive_like = 1")
    else:
        cur.execute("PRAGMA case_sensitive_like = 0")
    try:
        cur.execute(
            "SELECT entry_date, journal_entry FROM diary_entries"
            " WHERE journal_entry != '' AND entry_date BETWEEN ? AND ?  AND journal_entry LIKE ?",
             (fDate, tDate, str))
        d = cur.fetchall()
        # print(d)
        return d if d is not None else None
    except:
        return

def saveCategories(list):
    global cur
    cur.execute("DELETE FROM categories WHERE catId > 0" )
    for cat in list:
        cur.execute("INSERT INTO categories (name) VALUES(?)", (cat,))
    conn.commit()

def setDBTitle(title):
    global cur
    cur.execute("UPDATE categories SET DBTitle = ? \
         WHERE catID = ?", (title, 0))
    conn.commit()

def fetchDBInfo():
    global cur
    cur.execute("SELECT DBTitle, name FROM categories ")
    return cur.fetchall()

def updateEvent(evId, evData):
    global cur
    cur.execute("UPDATE diary_events SET Title = ?, StartDate = ?, Category = ?, Notes = ?,\
        ReminderDays = ?, DOB = ?, MonthDay = ?, Period = ?, NoOfTimes = ?, PeriodValue = ?,\
        CreationDate = ? WHERE EventNumber = ?",
        (evData["Title"], evData["StartDate"], evData["Category"], evData["Notes"],
         evData["ReminderDays"], evData["DOB"], evData["MonthDay"], evData["Period"],
         evData["NoOfTimes"], evData["PeriodValue"], evData["CreationDate"], evId))
    conn.commit()

def removeEvent(evId):
    global cur
    cur.execute("DELETE FROM diary_events WHERE EventNumber = ?", (evId,))
    conn.commit()

def insertEvent(evData):
    global cur
    cur.execute("INSERT INTO diary_events (Title, StartDate, Category, Notes, \
            ReminderDays, DOB, MonthDay, Period, NoOfTimes, PeriodValue, CreationDate)\
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    evData["Title"], evData["StartDate"], evData["Category"], evData["Notes"],
                    evData["ReminderDays"], evData["DOB"], evData["MonthDay"],
                    evData["Period"], evData["NoOfTimes"], evData["PeriodValue"],
                    evData["CreationDate"]))
    conn.commit()
    evNo = cur.lastrowid
    populateEntry(evNo)

def addEntry(entryDate, entry=''):
    global cur
    d = fetchEntry(entryDate)
    if d is not None:
        cur.execute("""UPDATE diary_entries SET journal_entry = ? \
         WHERE entry_date = ?""", (entry, entryDate))
        conn.commit()
        d = fetchEntry(entryDate)
        if d[0] == '' and d[1] == '':
            purgeEntries(entryDate)
    else:
        cur.execute("INSERT INTO diary_entries (entry_date, journal_entry) \
                VALUES (?, ?)", (entryDate, entry))
    conn.commit()

def populateEntry(rid=1, delete=False):
    global cur
    cur.execute("SELECT * FROM diary_events WHERE EventNumber = ?", (rid,))
    d = cur.fetchone()
    ev_no = d[0]
    ev_sdate = d[1]
    ev_monthday = int(d[8])
    if ev_monthday == 0: ev_monthday += 1
    ev_period = d[9]
    ev_times = d[10]
    ev_periodval =  d[12]
    if ev_monthday == eventEditDialog.MONTHWEEKDAY:
        monthday = ev_sdate.weekday()
    repRuleList = list(rrule(freq=periodDic[ev_period], interval=ev_periodval,
                             count=ev_times, dtstart=ev_sdate))
    for rdate in repRuleList:
        purge = False
        ev_date = datetime.date(rdate)
        cur.execute("SELECT * FROM diary_entries WHERE entry_date = ?", (ev_date,))
        entry = cur.fetchone()
        if entry is not None:
            if len(entry[2]) > 0 :
                ev_set = eval(entry[2])
            else:
                ev_set = set()
            if delete == False:
                ev_set.add(ev_no)
            else:
                if ev_no in ev_set:
                    ev_set.remove(ev_no)
                    if len(ev_set) == 0:
                        ev_set = ''
                if entry[1] == '' and ev_set == '':
                    purge = True
            cur.execute("UPDATE diary_entries SET event_list = ? WHERE entry_date = ?", \
                        (str(ev_set), ev_date))
        else:
            if delete == False:
                ev_set = set()
                ev_set.add(ev_no)
                cur.execute(
                    "INSERT INTO diary_entries(entry_date, event_list) VALUES (?, ?)",
                    (ev_date, str(ev_set)))
        conn.commit()
        if purge == True:
            purgeEntries(ev_date)

def purgeEntries(sDate, fDate=None):
    global cur
    cur.execute("DELETE FROM diary_entries WHERE entry_date = ?", (sDate,))
    conn.commit()

def populateEntries():
    global cur
    cur.execute("SELECT EventNumber FROM diary_events ")
    d = cur.fetchall()
    for d[0] in d:
        n = int(d[0][0])
        #         print (n)
        populateEntry(n)
    conn.close()


if __name__ == '__main__':
    populateEntries()
#     SQLiteFetchEntry()
#     PopulateEntries()
