import sqlite3
import uuid

# check if new record corresponds with existing UUID/SocialSec nr
    #if yes, update record
    #if no, create new record


# db tables: patientIds, journal
def if_patientID_exists(incoming_journal):

    return NotImplemented


connection = sqlite3.connect("journal.db")

cursor = connection.cursor()
  
connection.close()