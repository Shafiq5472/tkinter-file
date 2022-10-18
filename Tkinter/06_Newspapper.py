# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:04:49 2022

@author: shano
"""

from tkinter import *
from PIL import Image , ImageTk

root=Tk()
root.geometry("1300x750")
root.minsize(1300,850)
root.maxsize(1300,850)
root.title("Newspaper")
# scroll_bar = Scrollbar(root)
  
# scroll_bar.pack( side = RIGHT,fill = Y )
# mylist = Listbox(root, yscrollcommand = scroll_bar.set )


frame0=Frame(root)
frame0.pack(side=TOP,fill=X,padx=8,pady=8)
label0=Label(frame0,text="WORLD TIMES",font="comicsansms 20",bg="red",fg="white",borderwidth=5,relief=RIDGE)
label0.pack(side=TOP,fill=X)
label=Label(frame0,text="Date : 02-04-2020, Day : Thursday",font="comicsansms 13",fg="white",bg="red",borderwidth=5,relief=RIDGE)
label.pack(side=BOTTOM,fill=X)

frame1=Frame(root)
frame1.pack(side=TOP,fill=X)
label1=Label(frame1,text="Aaj ke Taaze Khabar !!",font="comicsansms 15 bold",borderwidth=5,relief=SUNKEN,bg="light blue")
label1.pack(side=TOP,fill=X,padx=8,pady=8)

frame2=Frame(root)
frame2.pack(anchor="nw")
p1 = Image.open("corona_virus.jpg")
photo1=ImageTk.PhotoImage(p1)
i1=Label(frame2,image=photo1,borderwidth=5,relief=GROOVE)
i1.pack(anchor="nw",side=LEFT,padx=15,pady=10)
label2=Label(frame2,text="The new coronavirus is forcing more top Israeli officials into isolation\
after the country's health minister,\n who has had frequent contact with Prime Minister Benjamin Netanyahu\
, tested positive, the Health\n Ministry said Thursday.\
The Middle East has over 78,000 confirmed cases of the virus, most of those in\n Iran, and over 3,500 deaths.\
Israel's health minister Yaakov Litzman and his wife, who also has\n contracted the virus, are in isolation, \
feel well and are being treated, the statement said. Requests\n to enter isolation will be sent to those who\
came in contact with the minister in the past two weeks,\n the announcement said.",font="comicsansms 15",bg="yellow",borderwidth=5,relief=GROOVE)
label2.pack(anchor="ne",side=LEFT,padx=15,pady=10)

frame3=Frame(root)
frame3.pack(anchor="ne",side=TOP)
p2 = Image.open("ww2.jpg")
photo2=ImageTk.PhotoImage(p2)
image2=Label(frame3,image=photo2,borderwidth=5,relief=GROOVE)
image2.pack(side=RIGHT,padx=15,pady=10)
label3=Label(frame3,text="World War II (often abbreviated to WWII or WW2), also known as the Second World War, was a\n\
global war that lasted from 1939 to 1945. The vast majority of the world's countries—including all the\n great powers—eventually\
formed two opposing military alliances: the Allies and the Axis. A state of total\n war emerged, directly involving more\
than 100 million people from more than 30 countries. The major\n participants threw their entire economic, industrial, and\
scientific capabilities behind the war effort, blurring\n the distinction between civilian and military resources.\
World War II was the deadliest conflict in human\n history, marked by 70 to 85 million fatalities, most of whom were\
civilians in the Soviet Union and China.\n It included massacres, genocides including the Holocaust, strategic bombing,\
premeditated death\n from starvation and disease, and the only use of nuclear weapons in war.",font="comicsansms 15",bg="orange",borderwidth=5,relief=GROOVE)
label3.pack(side=LEFT)

frame4=Frame(root)
frame4.pack(anchor="nw",side=TOP)
p3 = Image.open("comp.jpg")
photo3=ImageTk.PhotoImage(p3)
image3=Label(frame4,image=photo3,borderwidth=5,relief=GROOVE)
image3.pack(side=LEFT,padx=15,pady=10)
label4=Label(frame4,text='A computer is a machine that can be instructed to carry out sequences of arithmetic or\
logical operations\n automatically via computer programming. Modern computers have the\
ability to follow generalized\n sets of operations, called programs. These programs enable computers to perform an\
extremely wide\n range of tasks. A "complete" computer including the hardware, the operating system (main software), and\n\
peripheral equipment required and used for "full" operation can be referred to as a computer system.\
This term\n may as well be used for a group of computers that are connected and work\
together, in particular\n a computer network or computer cluster.',font="comicsansms 15",bg="green",borderwidth=5,relief=GROOVE)
label4.pack(side=RIGHT,padx=15,pady=10)

# mylist.pack( side = LEFT, fill = BOTH )
  
# scroll_bar.config(command = mylist.yview )
root.mainloop()