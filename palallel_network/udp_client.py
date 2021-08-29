#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:43:35 2017

@author: inoueshinichi
"""

""" udp_client.py """

import socket
from datetime import datetime

server_address = ('localhost', 6789)
max_size = 4096

print('Staring the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hey!', server_address)
data, server = client.recvfrom(max_size)
print('At', datetime.now(), server, 'said', data)
client.close()

