#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:48:08 2017

@author: inoueshinichi
"""

""" timeit.py """

from timeit import timeit
print(timeit('num = 5; num *= 2', number=1))
