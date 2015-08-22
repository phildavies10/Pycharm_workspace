from sqliteUtils import addEntry, fetchAllEvents, insertEvent
import datetime
from dateutil.parser import parse
from icalendar import Calendar, Event, vDate, Timezone, TimezoneStandard, TimezoneDaylight

numPeriod = {1: 'DAILY',
             2: 'WEEKLY',
             3: 'MONTHLY',
             4: 'YEARLY'
             }
periodNum = {'DAILY': 1,
             'WEEKLY': 2,
             'MONTHLY': 3,
             'YEARLY': 4
             }

def readIcs():
    file = open('phildavies10@gmail.ics', 'rb')
    cal = Calendar.from_ical(file.read())
    for event in cal.walk():
        evData = {}
        if event.name == "VEVENT":
            # if event.name == "VJOURNAL":
            evTitle = event.get('SUMMARY')
            if len(evTitle) > 0:
                evRrule = event.get('RRULE')
                evData["Period"] = 1
                evData["PeriodValue"] = 1
                evData["NoOfTimes"] = 1
                if evRrule:
                    for key in evRrule:
                        if key == 'FREQ':
                            evData["Period"] = periodNum[evRrule[key][0]]
                        if key == 'INTERVAL':
                            evData["PeriodValue"] = evRrule[key][0]
                            # print(evRrule[key][0])
                        if key == 'COUNT':
                            evData["NoOfTimes"] = evRrule[key]

                evStartDate = parse(event['DTSTART'].to_ical()).date()
                evCreatedDate = parse(event['CREATED'].to_ical()).date()
                evData["Title"] = evTitle
                evData["StartDate"] = evStartDate
                evData["CreationDate"] = evCreatedDate
                evData["Notes"] = event.get('DESCRIPTION')
                evData["Category"] = "None"
                evData["ReminderDays"] = None
                evData["DOB"] = None
                evData["MonthDay"] = 0
            # print(evData)
            insertEvent(evData)
    file.close()

def writeIcs():
    cal = Calendar()
    cal.add('PRODID', '-//Dayfacto Journal//dpd//')
    cal.add('VERSION', '1.0')
    cal.add('VERSION', 'GREGORIAN')
    timezone = Timezone()
    timezone.add('TZID', 'Europe/London')
    daylight = TimezoneDaylight()
    daylight.add('TZOFFSETFROM', datetime.timedelta(hours=0))
    daylight.add('TZOFFSETTO', datetime.timedelta(hours=1))
    daylight.add('TZNAME', 'BST')
    timezone.add_component(daylight)
    standard = TimezoneStandard()
    standard.add('TZNAME', 'GMT')
    standard.add('TZOFFSETFROM', datetime.timedelta(hours=1))
    standard.add('TZOFFSETTO', datetime.timedelta(hours=0))
    timezone.add_component(standard)
    cal.add_component(timezone)

    evtList = fetchAllEvents()
    count = 0
    for evt in evtList:
        event = Event()
        event.add('SUMMARY', evt[0])
        event.add('DTSTART', evt[2])
        if evt[5] > 1:
            event.add('RRULE', {'freq': numPeriod[evt[4]], 'interval': evt[6], 'count': evt[5]})
        event['uid'] = str(datetime.datetime.today().time()) + str(evt[8]) \
                       + 'phildavies10@gmail.com'
        # event.add('DESCRIPTION', 'This is another description')
        # event.add('VJOURNAL', 'This is another journal entry')
        cal.add_component(event)
        # print(numPeriod[evt[4]])
        count += 1
    print(count)
    f = open('example.ics', 'wb')
    f.write(cal.to_ical())
    f.close()

if __name__ == '__main__':
    # readIcs()
    writeIcs()