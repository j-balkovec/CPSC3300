"""__doc__
__auth__: Jakob Balkovec
__version__: 1.0
__date__: 2024-03-03
__status__: Done
__file__: secrets.py

__desc__: File that contains all the secrets for the Flask application. 
          This file (will be)/is used to store all the sensitive information

__bugs__: None

__attention__: Clear contents before pushing to git
"""

import os

# Define database password (replace placeholder with actual password)
PASSWORD = 'Jakob123!'

# Define debugger pin
DEBUGGER_PIN = 128-738-709

# Database Configuration
# Replace the placeholders with actual database credentials and settings

# Define database connection parameters
DATABASES = {
    'default': {
        'NAME': 'Project1',                       # Database name
        'USER': 'root',                           # Database user
        'PASSWORD': PASSWORD,                     # Database password
        'HOST': 'localhost',                      # Database host
        'PORT': '3306',                           # Database port
    }
}

# Construct database URI using database connection parameters
DATABASE_URI = f"mysql://{DATABASES['default']['USER']}:{DATABASES['default']['PASSWORD']}@{DATABASES['default']['HOST']}:{DATABASES['default']['PORT']}/{DATABASES['default']['NAME']}"

# Define Flask secret key
SECRET_KEY = 'neruighbequrhbvqaosiu;decnzsDFIJQWEOIUFHAERSOD;IVCBNASDIUL;FHJASEIULFASH'

# Define directory for log files
LOG_DIR = 'logs'

# Construct log directory path
LOG_DIR = os.path.join(os.getcwd(), 'logs')

# Construct log file path
LOG_FILE = os.path.join(LOG_DIR, 'flask.log')

# Define log format
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Ensure log directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Function to clear log file
def clear_log_file():
    """
    Function to clear the contents of the log file.
    """
    with open(LOG_FILE, 'w') as log_file:
        log_file.write('')

# Logging configuration
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