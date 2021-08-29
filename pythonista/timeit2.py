#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:50:04 2017

@author: inoueshinichi
"""

""" timeit2.py """

from timeit import repeat
print(repeat('num = 5; num *= 2', number=1, repeat=3))

