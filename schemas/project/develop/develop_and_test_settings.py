"""
Common development settings.
"""
from schemas.project.default.settings import *  # noqa

THIS_DIR = os.path.dirname(__file__)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'schemas',
        'USER': os.environ.get('POSTGRES_USER', 'schemas'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '1234'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, ssl_require=True)
DATABASES['default'].update(db_from_env)

# celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

REDIS_HOST = 'schemas_1'
REDIS_PORT = 6379