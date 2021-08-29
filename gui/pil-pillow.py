#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:35:38 2017

@author: inoueshinichi
"""

""" pil-pillow.py """

from PIL import Image
img = Image.open('python3.jpg')
print(img.format)
print(img.size)
print(img.mode)
img.show()

crop = (55, 70, 85, 100)
img2 = img.crop(crop)
img2.show()
