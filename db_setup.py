import sqlite3
import uuid
import datetime


def read_record():
    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()
    cursor.execute("select * from journal")
    entries = cursor.fetchall()
    for row in entries:
        print(row)
    connection.close()


def create_database():

    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()

    cursor.execute("create table journal (patientId text, documentType text, version integer, savedTimeStamp timestamp)")

    cursor.execute("create table patientIds (socialSecurityNumber integer, patientID text)")
    connection.close()


def crate_fake_data():

    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()

    sql_insert = f"""
    INSERT INTO patientIds (socialSecurityNumber, patientID)
    VALUES (?, ?)
    """

    for entry in patientIds:
        cursor.execute(sql_insert, (entry["socialSecurityNumber"], entry["patientId"]))

    sql_insert2 = """
    INSERT INTO journal (patientId, documentType, version, savedTimeStamp)
    VALUES (?, ?, ?, ?)
    """
    
    for entry in journal:
        cursor.execute(sql_insert2, (entry["patientId"], entry["documentType"], entry["version"], entry["savedTimeStamp"]))

    connection.commit()
    connection.close()


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

create_database()
crate_fake_data()
read_record()