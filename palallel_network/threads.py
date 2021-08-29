#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 07:35:47 2017

@author: inoueshinichi
"""

""" threads.py """

import threading

def do_this(what):
    whoami(what)
    
def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))
    

if __name__ == "__main__":
    whoami("I'm the main prgram")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function %s" % n,))
        p.start()
        
