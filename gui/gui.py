#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:22:53 2017

@author: inoueshinichi
"""

""" tkinter.py """

import tkinter
from PIL import Image, ImageTk

main = tkinter.Tk()
img = Image.open('python3.jpg')
tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()
