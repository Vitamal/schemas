from schemas.project.default.settings import *  # noqa

DEBUG = False

INSTALLED_APPS += [
    'gunicorn',
]

# The SECRET_KEY MUST be set as an environment variable in prod
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Set this to True to avoid transmitting the session cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True

# Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
CSRF_COOKIE_SECURE = True


###########################
# Database
###########################
DATABASES = {}

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES['default'] = dj_database_url.config()


###########################
# Templates
###########################
TEMPLATES[0]['OPTIONS']['debug'] = False



LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s %(asctime)s %(name)s %(pathname)s:%(lineno)s] %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            # This filter will only pass on records when settings.DEBUG is False.
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.db': {
            'handlers': ['console'],
            'level': 'INFO',  # Do not set to debug - logs all queries
            'propagate': False
        },
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        }
    }
}
