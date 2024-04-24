from datetime import datetime
import csv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from models.incoming_journal import IncomingJournal


class CSVEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_file() and event.src_path.endswith(".csv"):
            print(f"New CSV file created: {event.src_path}")
            self.read_csv(event.src_path)

    def read_csv(self, filepath):

        with open(filepath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            
            next(reader, None)

            for row in reader:
                changed_journal_record((IncomingJournal(row[0], row[1], row[2], row[3], row[4])))

def listen_to_new_csv():
    watch_dir = "./csv" 
    observer = Observer()

    observer.schedule(CSVEventHandler(), watch_dir, recursive=True)
    observer.start()

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    


    return None

def changed_journal_record(incoming_journal):

    # now = datetime.now()
    # timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # incoming_journal = {
    #         "socialSecurityNumber" : 8403120382, #dd03713c-1f3c-4096-852a-29191ff6b191
    #         "documentType" : "string",
    #         "version" : 2,
    #         "timeStamp" :timestamp,
    #         "savedTimeStamp" : timestamp,
    #     }

    return incoming_journal

if __name__ == '__main__':
    print(changed_journal_record())