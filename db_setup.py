import sqlite3
import uuid
import datetime

journal = [
{
    "patientId" : "AA03713c-1f3c-4096-852a-29191ff6b188",
    "documentType" : "Kemlab",
    "version" : 1,
    "savedTimeStamp" : datetime.datetime.now()
},
{
    "patientId" : str(uuid.uuid4()),
    "documentType" : "Multilab",
    "version" : 3,
    "savedTimeStamp" : datetime.datetime.now()
},
{
    "patientId" : str(uuid.uuid4()),
    "documentType" : "Blodlab",
    "version" : 6,
    "savedTimeStamp" : datetime.datetime.now()
},
    {
    "patientId" : str(uuid.uuid4()),
    "documentType" : "Röntgen",
    "version" : 2,
    "savedTimeStamp" : datetime.datetime.now()
},
]

patientIds = [
  {
    "socialSecurityNumber": 1234567890,  
    "patientId": str(uuid.uuid4())
  },
  {
    "socialSecurityNumber": 9876543210, 
     "patientId": str(uuid.uuid4())
  },
  {
    "socialSecurityNumber": 216543210, 
     "patientId": str(uuid.uuid4())
  },
    {
    "socialSecurityNumber": 8508120386, 
     "patientId": "AA03713c-1f3c-4096-852a-29191ff6b199"
  }
]

def connect_and_execute(sql, params=()):
    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()
    cursor.execute(sql, params)
    connection.commit()
    connection.close()


def create_tables():
    sql_create_journal = """
    CREATE TABLE IF NOT EXISTS journal (
        id INTEGER PRIMARY KEY,
        patientId TEXT,
        documentType TEXT,
        version INTEGER,
        savedTimeStamp TIMESTAMP
    );
    """

    sql_create_patientIds = """
    CREATE TABLE IF NOT EXISTS patientIds (
        id INTEGER PRIMARY KEY,
        socialSecurityNumber INTEGER,
        patientId TEXT
    );
    """
    connect_and_execute(sql_create_journal)
    connect_and_execute(sql_create_patientIds)


def create_fake_data(patientIds, journal):
    for entry in patientIds:
        insert_data("patientIds", entry)

    for entry in journal:
        insert_data("journal", entry)


def insert_data(table, data):
    sql_insert = f"""
    INSERT INTO {table} ({', '.join(data.keys())})
    VALUES ({', '.join(['?'] * len(data))})
    """
    params = [value for value in data.values()]
    connect_and_execute(sql_insert, params)


def read_data(table):
    sql_select = f"SELECT * FROM {table}"
    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()
    cursor.execute(sql_select)
    entries = cursor.fetchall()
    connection.close()
    return entries

create_tables()

create_fake_data(patientIds=patientIds, journal=journal)

entries = read_data("journal")
for row in entries:
    print(row)
