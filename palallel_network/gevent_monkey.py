#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:42:10 2017

@author: inoueshinichi
"""

""" gevent_monkey.py """

import gevent
from gevent import monkey; monkey.patch_all()
import socket

hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 
        'www.antique-taxidermy.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
    
