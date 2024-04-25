import json
from kafka import KafkaConsumer

from database.db_client import persist_patient_record

if __name__ == '__main__':

    consumer = KafkaConsumer(
        "journal",
        bootstrap_servers='localhost:29092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        persist_patient_record(json.loads(message.value))