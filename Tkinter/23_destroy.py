# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 14:21:44 2022

@author: shano
"""

from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("CodeWithHarry - Title Of My GUI")
root.wm_iconbitmap("1.ico")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command = root.destroy).pack()

root.mainloop()