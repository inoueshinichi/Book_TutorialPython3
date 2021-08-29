#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:53:06 2017

@author: inoueshinichi
"""

""" knock_server.py """

from twisted.internet import protocol, reactor


class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print 'Client:', data
        if data.startswith("Knock knock"):
            response = "Who's there?"
        else:
            response = data + " who?"
        print 'Server:', response
        self.transport.write(response)
        
class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()
    
reactor.listenTCP(8000, KnockFactory())
reactor.run()

