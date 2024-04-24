#!/bin/sh

python -m venv venv
source venv/bin/activate
docker-compose -f config/docker-compose.yml up -d
pip install -r requirements.txt
PYTHONPATH=. python3 database/db_client.py