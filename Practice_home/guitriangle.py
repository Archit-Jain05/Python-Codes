import tkinter
from tkinter import *

def pb():
    print(type(data.get()))

win1=Tk()
win1.title("Triangle Area Calculator")
win1.geometry('500x500')

l1=Label(win1,text="Enter height:",font=("Arial",20))
data=IntVar()
tb1=Entry(win1,textvariable=data)

b1=Button(win1,text="Calculate",command=pb)
l1.grid(row=0,column=0)
l1.pack()
b1.pack()
tb1.pack()
win1.mainloop()

