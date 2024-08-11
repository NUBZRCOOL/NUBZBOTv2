import os
from os.path import abspath, dirname
import logging

os.chdir(dirname(abspath(__file__)))

parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logFile = os.path.join(parentDir, "log.txt")

def setUp():

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(levelname)s - %(name)s - %(asctime)s >> %(message)s',
                "datefmt": "%a %b %d, %Y %I:%M:%S %p"
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': logFile,
            },
        },
        'loggers': {
            '': {  # Root logger
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'hikari': {  # Hikari logger
                'handlers': ['file'],
                'level': 'INFO',  # Adjust level as needed
                'propagate': False,
            },
            'lightbulb': {  # Lightbulb logger
                'handlers': ['file'],
                'level': 'INFO',  # Adjust level as needed
                'propagate': False,
            },
        }
    })

logger = logging.getLogger(__name__)
setUp()