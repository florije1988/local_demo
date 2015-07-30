# -*- coding: utf-8 -*-
__author__ = 'florije'

import logging
import logging.config

# load my module

import my_module

# load the logging configuration

# logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

logging_config = dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        'format': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    handlers={
        'sh': {'class': 'logging.StreamHandler',
               'formatter': 'format',
               'level': logging.DEBUG},
        'fh': {
            'class': 'logging.FileHandler',
            'formatter': 'format',
            'level': logging.DEBUG
        }
    },
    loggers={
        '': {'handlers': ['sh'],
             'level': logging.DEBUG}
    }
)

another_config = {
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)


logger.info('start.')

my_module.foo()
bar = my_module.Bar()
bar.bar()

logger.info('end.')
