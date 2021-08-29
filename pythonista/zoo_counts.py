#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:37:55 2017

@author: inoueshinichi
"""

""" zoo_counts.py """

import csv
from collections import Counter

counts = Counter()
with open('zoo.csv', 'rt') as fin:
    cin = csv.reader(fin)
    for num, row in enumerate(cin):
        if num > 0:
            counts[row[0]] += int(row[-1])

print(counts.items())
for animal, hush in counts.items():
    print("%10s %10s" % (animal, hush))
    
