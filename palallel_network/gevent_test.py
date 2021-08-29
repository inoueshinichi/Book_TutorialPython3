#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:31:07 2017

@author: inoueshinichi
"""

""" gevent_test.py """

import gevent
from gevent import socket

hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 
        'www.antique-taxidermy.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
    
    