web: gunicorn schemas.wsgi --log-file -
worker: celery -A schemas worker -l INFO
