import sqlite3
import uuid

from models.persisted_journal import PersistedJournal

    
def write_patientId(socialSecurityNumber, patientId):
    
    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()

    sql_insert = f"""
    INSERT INTO patientIds (socialSecurityNumber, patientID)
    VALUES (?, ?)
    """
    cursor.execute(sql_insert, (socialSecurityNumber, patientId))

    connection.commit()
    connection.close()

def write_record(persisted_journal):
    
    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()

    sql_insert = f"""
    INSERT INTO journal (patientId, documentType, version, savedTimeStamp)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(sql_insert, (PersistedJournal(persisted_journal["patientId"], persisted_journal["version"], persisted_journal["documentType"], persisted_journal["savedTimeStamp"])))

    connection.commit()
    connection.close()

def if_patientId_exists(incoming_journal):

    socialSecurityNumber = incoming_journal["socialSecurityNumber"]

    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()
    sql = "SELECT patientId FROM patientIds WHERE socialSecurityNumber = ?"
    cursor.execute(sql, (socialSecurityNumber,))
    result = cursor.fetchone()
    connection.close()

    patient = PersistedJournal(None, incoming_journal["version"], incoming_journal["documentType"], incoming_journal["savedTimeStamp"])

    if result:
        PersistedJournal["patientId"] = result[0]
        return write_record(patient)
    else:
        PersistedJournal["patientId"] =  uuid.uuid4()
        return write_patientId(incoming_journal["socialSecurityNumber"], PersistedJournal["patientId"])

def read_record():
    connection = sqlite3.connect("journal.db")
    cursor = connection.cursor()
    cursor.execute("select * from journal")
    entries = cursor.fetchall()
    print(entries)
    connection.close()
