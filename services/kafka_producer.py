from dataclasses import asdict
from datetime import datetime
import json
from services.csv_reader import read_csv
from kafka import KafkaProducer
from watchfiles import Change, watch

def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=serializer
)

if __name__ == '__main__':

    for changes in watch("./csv"):
        for changetype, path in changes:
            if changetype != Change.added:
                continue
            for message in read_csv(path):
                print (f'Producing message @ {datetime.now()} | Message = {str(message)}')
                producer.send('test', asdict(message))