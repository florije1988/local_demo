# -*- coding: utf-8 -*-
__author__ = 'florije'

import logging
import logging.config

# load my module

import my_module

# load the logging configuration

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

logger.info('start.')

my_module.foo()
bar = my_module.Bar()
bar.bar()

logger.info('end.')
