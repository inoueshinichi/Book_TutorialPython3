#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:21:57 2017

@author: inoueshinichi
"""

""" capitals2.py """

def process_cities(filename):
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            #if 'quit' in line.lower():
            if 'quit' == line.lower():
                return
            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')
            
if __name__ == '__main__':
    import sys
    process_cities(sys.argv[1])