import tkinter as tk

m=tk.Tk()

b1=tk.Button(m,text='Hello world',width=15,height=10)
l=tk.Entry(m,{},width=40)
b1.pack()
l.pack()
m.title('Trial')
m.mainloop()