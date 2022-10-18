# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:27:15 2022

@author: shano
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("My Frame GUI")

root.geometry("999x555")
root.resizable(False,False)

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")
l1 = Label(f1,text = "Assalam o Alaikum How are you peaple we are here for you what kind of help do you you want")
l1.pack(pady = 184)
f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")
l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()


root,mainloop()