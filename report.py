#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:17:29 2017

@author: inoueshinichi
"""

""" report.py """
def get_description():
    """ プロと同じようにランダムな天気を返す"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
