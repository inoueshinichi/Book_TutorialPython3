#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:31:07 2017

@author: inoueshinichi
"""

""" weather.py """
from sources import daily, weekly

print("Daily forcast:", daily.forecast())
print("Weekly forcast:", weekly.forcast())

for number, outlook in enumerate(weekly.forcast(), 1):
    print(number, outlook)
    
    