# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:32:49 2022

@author: shano
"""

from tkinter import *
from PIL import Image ,ImageTk

root = Tk()
root.title("TRY")
root.geometry("744x444")
# root.maxsize(1024,677)
# root.minsize(744,322)
label= Label(text = '''Hello  peaple how are uh here is my frist Gui file in python using Tkinter labrary'''
             ,fg = 'white',bg ='red',font =("Arial","18","bold","italic","underline"),padx="15",pady = "15"
             ,relief = SUNKEN )
label.pack(anchor='nw',side='left' ,fill='x')

a = Image.open("1.jpg")
b = ImageTk.PhotoImage(a)

Label(image=b).pack(anchor='nw',side="bottom")

root.mainloop()