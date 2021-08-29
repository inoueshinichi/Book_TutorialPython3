#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:12:04 2017

@author: inoueshinichi
"""

""" mp.py """
"""
multiprocessingによるプロセスの作成
"""

import multiprocessing
import os

def do_this(what):
    whoami(what)
    
def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))
    
if __name__ == "__main__":
    whoami("I'm the main program")
    whoami("I'm the main program 2")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,
                                    args=("I'm function %s" % n,))
        p.start()
        
