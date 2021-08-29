#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:09:48 2017

@author: inoueshinichi
"""

""" knock_client.py """

from twisted.internet import reactor, protocol


class KnockClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Knock knock")
        
    def dataReceived(self, data):
        if data.startswith("Who's there?"):
            response = "Disappearing client"
            self.transport.write(response)
        else:
            self.transport.loseConnection()
            reactor.stop()
    
class KnockFactory(protocol.ClientFactory):
    protocol = KnockClient
    
    
def main():
    f = KnockFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()
    
if __name__ == '__main__':
    main()
    
