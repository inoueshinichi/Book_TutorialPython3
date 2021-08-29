#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:47:23 2017

@author: inoueshinichi
"""

""" bottle_test.py """

import requests

resp = requests.get('http://localhost:9999/echo/Mothra')
if resp.status_code == 200 and resp.text == 'Say hello to my little friend: Mothra!':
        print('It worked! That almost never happens!')
else:
    print('Argh, got this:', resp.text)
    
