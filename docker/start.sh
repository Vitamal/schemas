#!/bin/bash

set -e

#waiting for postgres
until $(nc -z ${DB_HOST} ${DB_PORT})
do
  echo "Waiting for PostgreSQL..."
  echo "${DB_HOST}-${DB_PORT}"
  sleep 3
done


#start the celery
celery -A schemas worker -l INFO &

#start the server
python manage.py migrate
python manage.py loaddata db_dumps/development_database.json
python manage.py runserver 0.0.0.0:8000
