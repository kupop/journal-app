# Kafka Journal Flow Demo
A first version of a real-time journal flow using Apache Kafka in which records are saved to an SQL-database.

## 1. Installation Requirements:
This project requires python and docker (including docker-compose) to run.

## 2. Usage Instructions:
Run setup.sh. This gets kafka and zookeeper containers up and running, installs the SQLite database with some sample data, installs the python packages used and sets up your virtual environment.

Run run_consumer.sh and run_producer.sh in separate terminals to start the kafka client and producer. Drop a .csv-file matching the format of example.csv into the incoming_journal_entries folder to start the data flow.

New kafka messages will be printed to the terminal.

To make SQL-queries, insert the queries into db_client.py into the read_record(). Run file with "PYTHONPATH=. python3 database/db_client.py" from console in project root folder.

## 3. Features:
This project demonstrates leveraging kafka to simulate a simple journal system. It uses a csv-filewatcher to simulate incoming messages and SQLite as a placeholder for a full SQL-compatible database solution.

## 4. Technologies Used:
kafka-python, watchfiles, docker

## 5. Planning board for project:
https://github.com/users/kupop/projects/2

## 6. Currently out of scope/ possible future implementations
Schema registration  
Tests  
Security in the form of data-access  
Error handling  
Logging  
