#!/bin/bash

# start the redis
service redis-server start

#start the celery
celery -A schemas worker -l INFO &

#start the server
python manage.py runserver

service redis-server stop