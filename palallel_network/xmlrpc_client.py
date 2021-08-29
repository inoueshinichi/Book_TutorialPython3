#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:37:21 2017

@author: inoueshinichi
"""

""" xmlrpc_client.py """

import xmlrpc.client


proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
num = 7
result = proxy.double(num)
print("Double %s is % s" % (num, result))

