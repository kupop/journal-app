from datetime import datetime
import csv
from models.incoming_journal import IncomingJournal

def read_csv(filepath):

    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader, None) # ditch header
        for row in reader:
            yield IncomingJournal(row[0], row[1], int(row[2]), row[3], row[4])
