# 2 grid()

from tkinter import*

root = Tk()       # This Tk() method creates a basic root window which we see in every application we use

myLabel1 = Label(root, text="Hello World", cursor="dot", bg="black", fg="white")
myLabel2 = Label(root, text="Hello Kishore", padx=50, pady=50, underline=8)
myLabel3 = Label(root, text="Hello Sai")
myLabel4 = Label(root, text="Hello Varma")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)
myLabel4.grid(row=3, column=0)


root.mainloop()