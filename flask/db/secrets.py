"""DO NOT COMMIT THIS FILE TO GITHUB"""

import os

PASSWORD = 'Jakob123!'

DEBUGGER_PIN = 128-738-709

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Project1',
        'USER': 'root',
        'PASSWORD': PASSWORD,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DATABASE_URI = f"mysql://{DATABASES['default']['USER']}:{DATABASES['default']['PASSWORD']}@{DATABASES['default']['HOST']}:{DATABASES['default']['PORT']}/{DATABASES['default']['NAME']}"

SECRET_KEY = 'neruighbequrhbvqaosiu;decnzsDFIJQWEOIUFHAERSOD;IVCBNASDIUL;FHJASEIULFASH'

LOG_DIR = 'logs'

LOG_DIR = os.path.join(os.getcwd(), 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'flask.log')
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def clear_log_file():
    with open(LOG_FILE, 'w') as log_file:
        log_file.write('')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': LOG_FORMAT,
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'flask.log'),
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

