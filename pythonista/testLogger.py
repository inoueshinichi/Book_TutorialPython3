#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:35:34 2017

@author: inoueshinichi
"""

""" testLogger.py """

import logging

logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logger = logging.getLogger('bunyan')
logger.debug("Where's my axe?")
logger.warning("I need my axe")

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('banyan2')
logger.error("Where's my other plaid shirt?")



