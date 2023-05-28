import tkinter 
from tkinter import *
from tkinter import font as tkFont

root=Tk()
root.title("Hello world")
root.geometry("300x300")
root.resizable(False,False)

l1=Label(root,text="Hello world")
l1.place(x=200,y=150)
root.mainloop()