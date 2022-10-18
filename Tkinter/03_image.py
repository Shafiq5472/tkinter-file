# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:39:51 2022

@author: shano
"""

from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry("1024x644")

image = Image.open("1.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image=photo).pack()


root.mainloop()