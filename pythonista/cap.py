#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 09:08:53 2017

@author: inoueshinichi
"""

""" cap.py """

def just_do_it(text):
    # "<text>に含まれるすべての単語をタイトルケースに"
    """
    >>> just_do_it('duck')
    'Duck'
    >>> just_do_it('a veritable flock of ducks')
    'A Veritable Flock Of Ducks'
    >>> just_do_it("I'm fresh out of ideas")
    "I'm Fresh Out Of Ideas"
    """
    
    #return text.capitalize()
    #return text.title()
    from string import capwords
    return capwords(text)


if __name__ == '__main__':
    import doctest
    doctest.testmod()