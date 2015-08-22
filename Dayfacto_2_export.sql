
-- Table: categories
CREATE TABLE categories ( 
    catId   INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    catType TEXT,
    DBTitle TEXT 
);


-- Table: diary_events
CREATE TABLE diary_events ( 
    EventNumber  INTEGER PRIMARY KEY ASC AUTOINCREMENT
                         UNIQUE,
    StartDate    DATE    NOT NULL,
    EndDate      DATE,
    DOB          DATE,
    CreationDate DATE,
    Title        TEXT,
    Notes        TEXT,
    Category     TEXT    NOT NULL,
    MonthDay     INTEGER DEFAULT ( 0 ),
    Period       INTEGER,
    NoOfTimes    INTEGER DEFAULT ( 1 ),
    ReminderDays INTEGER,
    PeriodValue  INTEGER DEFAULT ( 0 ) 
);


-- Table: diary_entries
CREATE TABLE diary_entries ( 
    entry_date    DATE PRIMARY KEY
                       UNIQUE ON CONFLICT FAIL,
    journal_entry TEXT DEFAULT ( '' ),
    event_list    TEXT DEFAULT ( '' ) 
);

