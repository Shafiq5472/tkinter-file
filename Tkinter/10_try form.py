# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 18:36:18 2022

@author: shano
"""

from tkinter import *
from PIL import Image,ImageTk

f1 = Tk()
f1.title("Shanu")

f1.geometry("777x333")
#f1  = Frame(root,relief = SUNKEN).pack(side = RIGHT)
def H():
    print("text variable")
a = Label(f1,text = "first")
a.grid()
a1 = Entry(f1,textvariable= StringVar())
a1.grid(column = 1,row = 0)
b = Label(f1,text = "Second")
b.grid()
b1 = Entry(f1,textvariable= StringVar())
b1.grid(column = 1,row = 1)
c = Label(f1,text = "Third")
c.grid()
c1 = Entry(f1,textvariable= StringVar())
c1.grid(column = 1,row = 2)
d = Label(f1,text = "Fourth")
d.grid()
d1 = Entry(f1,textvariable= StringVar())
d1.grid(column = 1,row = 3)
f = Label(f1,text = "Fifth")
f.grid()
f2 = Entry(f1,textvariable= StringVar())
f2.grid(column = 1,row = 4)
g = Label(f1,text = "Sixth")
g.grid()
g1 = Entry(f1,textvariable= StringVar())
g1.grid(column = 1,row = 5)
h = Label(f1,text = "Seventh")
h.grid()
h1 = Entry(f1,textvariable= StringVar())
h1.grid(column = 1,row = 6)

Button(f1,text = "Submit",command = H).grid()

f1.mainloop()
