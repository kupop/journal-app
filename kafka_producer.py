from datetime import datetime
import time
import json
import random
from journal_event import changed_journal_record
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

#går bara in i loopen om filen körs separat
if __name__ == '__main__':
    # make program run until killed
    while True:
        message = changed_journal_record()

        print (f'Producing message @ {datetime.now()} | Message = {str(message)}')
        producer.send('test', message)    

        #spacing out messages to simulate spacing of events
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)
