import json
from kafka import KafkaConsumer

from database.db_client import persist_patient_record

if __name__ == '__main__':

    consumer = KafkaConsumer(
        "test",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        persist_patient_record(json.loads(message.value))