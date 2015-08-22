'''
Created on 27 Feb 2015

@author: phil
'''

import sqlite3
import os
from datetime import *
from dateutil.parser import parse
from dateutil.rrule import rrule, DAILY, WEEKLY, MONTHLY, YEARLY
import eventEditDialog

(NA, DAYS, WEEKS, MONTHS, YEARS) = range(5)
periodDic = {'One off': 1,
             'Daily': 1,
             'Weekly': 2,
             'Monthly': 3,
             'Yearly': 4
             }
#
# numPeriod = {1:'DAILY',
#              2:'WEEKLY',
#              3:'MONTHLY',
#              4:'YEARLY'
#              }


# print(os.path)
dbFile = "C:\\PyCharm workspace\\DayfactoPyCharm\\Dayfacto_2.db"
create = os.path.exists(dbFile)
if create:
    conn = sqlite3.connect(dbFile, detect_types=sqlite3.PARSE_DECLTYPES\
                           |sqlite3.PARSE_COLNAMES|sqlite3.PARSE_COLNAMES) 
cur = conn.cursor()

def parse_entries(file_name):
    entries_lines = {}
    line_count = 0
    with open(file_name) as entries_file:
        for line in entries_file.readlines():
            split_line = line.split('^')
            if len(split_line[1]) < 2:
                continue
            # print(split_line)
            e_date = parse(split_line[0], dayfirst='true')
            entry_date = datetime.date(e_date) 
            entry_text = split_line[1]
            event_list = ''
            if len(entry_text) >1:
                entries_lines[entry_date] = entry_text
                line_count += 1
    # print(entries_lines)
    # print ('Line count =', line_count )
    return entries_lines

def parse_events(file_name):
    events_lines = {}
    ev_no = 0
    with open(file_name) as entries_file:
        for line in entries_file.readlines():
            split_line = line.split('^')
            start_date = datetime.date(parse(split_line[1], dayfirst='true'))
            end_date = datetime.date(parse(split_line[3], dayfirst='true'))
            dob = None
            if len(split_line) > 7:
                dob = datetime.date(parse(split_line[7], dayfirst='true'))
            title = split_line[0]
            category = split_line[2]
            no_of_times = int(split_line[6])
            periodValue = int(split_line[5])
            period = periodDic[split_line[4]]
            ev_no += 1
            events_lines[ev_no] = [start_date, end_date, dob, title, category, \
                                    period, periodValue, no_of_times]
    # print ('Event count =', ev_no)
    return events_lines

def populateEntry(rid=1, delete=False):
    global cur
    cur.execute("SELECT * FROM diary_events WHERE EventNumber = ?", (rid,))
    d = cur.fetchone()
    print('Fetched event: ', d)
    ev_no = d[0]
    ev_sdate = d[1]
    ev_monthday = int(d[8])
    if ev_monthday == 0:
        ev_monthday += 1
    ev_period = d[9]
    ev_times = d[10]
    ev_periodval = d[12]
    if ev_monthday == eventEditDialog.MONTHWEEKDAY:
        monthday = ev_sdate.weekday()
    # print(numPeriod[ev_period], ev_periodval, ev_times, ev_sdate)
    repRuleList = list(rrule(freq=ev_period, interval=ev_periodval,
                             count=ev_times, dtstart=ev_sdate))
    # print(repRuleList)
    for rdate in repRuleList:
        purge = False
        ev_date = datetime.date(rdate)
        cur.execute("SELECT * FROM diary_entries WHERE entry_date = ?", (ev_date,))
        entry = cur.fetchone()
        if entry is not None:
            if len(entry[2]) > 0:
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
    # print('PURGE ', end='')
    # print(sDate)

def populateEntries():
    global cur
    cur.execute("SELECT EventNumber FROM diary_events ")
    d = cur.fetchall()
    for d[0] in d:
        n = int(d[0][0])
        #         print (n)
        populateEntry(n)
    conn.close()

# if __name__ == '__main__':
#     entries_dict = parse_entries('D:\\Documents\\Diaries\\DFPython\\Entries from '
#                                  '16-05-2015_^.txt')
#     entry_count = 0
#     for key in entries_dict:
#         d = entries_dict[key]
#         # print(key, d)
#         try:
#             cur.execute("INSERT INTO diary_entries(entry_date, journal_entry) VALUES (?, ?)",
#                         (key, d))
#             conn.commit()
#             entry_count += 1
#             print(key, d)
#             print('Entry count =', entry_count)
#         except:
#             conn.close()
#     conn.close()

if __name__ == '__main__':
    events_dict = parse_events \
        ('D:\\Documents\\Diaries\\DFPython\\Events from '
         '16-05-2015_^.txt')
    event_count = 0
    for key in events_dict:
        d = events_dict[key]
        print('Parsed event: ', d)
        # try:
        cur.execute("INSERT INTO diary_events (Title, StartDate, Category, Notes, \
                ReminderDays, DOB, MonthDay, Period, NoOfTimes, PeriodValue, CreationDate)\
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (d[3], d[0], d[4], None, None, d[2], 0, d[5], d[7], d[6], None))
        conn.commit()
        populateEntry(cur.lastrowid )
        event_count += 1
        # print('Event count =', event_count)
        # except:
        #     conn.close()
    # print(events_dict)
    conn.close()

# if __name__ == '__main__':
#     for e in range(396, 409):
#         populateEntry(e)
#     conn.close()