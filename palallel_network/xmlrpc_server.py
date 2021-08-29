#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:33:26 2017

@author: inoueshinichi
"""

""" xmlrpc_server.py """

from xmlrpc.server import SimpleXMLRPCServer

def double(num):
    return num * 2

server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(double, "double") # クライアントがサーバーの関数double(num)を使えるように登録
server.serve_forever()

