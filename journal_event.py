from datetime import datetime

#fake record
def changed_journal_record():

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    journal_record = {
        "patient_id" : "UUID4",
        "record_type" : "string",
        "version" : 1,
        "saved_time" : timestamp,
    }

    return journal_record

if __name__ == '__main__':
    print(changed_journal_record())