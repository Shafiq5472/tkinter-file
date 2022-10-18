# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 19:40:39 2022

@author: shano
"""

from tkinter import *

root = Tk()

# Width x Height
root.geometry("644x434")

# width, height
root.minsize(300,100)

# width, height
root.maxsize(1200, 988)

Label(text="Shanu is a good boy and this is his GUI").pack()


root.mainloop()