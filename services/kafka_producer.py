from datetime import datetime
import time
import json
import random
from services.journal_event import changed_journal_record
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        message = changed_journal_record()

        print (f'Producing message @ {datetime.now()} | Message = {str(message)}')
        producer.send('test', message)    

        #spacing out messages to stand looking at them in a terminal
        time_to_sleep = random.randint(1, 5)
        time.sleep(time_to_sleep)
