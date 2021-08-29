#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:41:48 2017

@author: inoueshinichi
"""

""" sqlAlchemy.py """

import sqlalchemy as sa

conn = sa.create_engine('sqlite:///memory') # sqlite:// + /memory
conn.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY,
                                  count INT, damages FLOAT)''')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)

rows = conn.execute('SELECT * FROM zoo')
print(rows)

for row in rows:
    print(row)
    
print('------')
