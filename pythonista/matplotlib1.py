#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 21:31:27 2017

@author: inoueshinichi
"""

""" matplotlib1.py """

import matplotlib.pyplot as plot
import matplotlib.image as image

img = image.imread('python3.jpg')
plot.imshow(img)
plot.show()
