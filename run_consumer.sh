#!/bin/sh

source venv/bin/activate
PYTHONPATH=. python3 services/kafka_consumer.py