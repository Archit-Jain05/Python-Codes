import tkinter as tk

m=tk.Tk()

b1=tk.Button(m,text='Hello world',width=150,height=30,command=m.destroy)
b1.pack()
m.title('Trial')
m.mainloop()