#Program to add radio buttons in Tkinter 

from tkinter import *

root = Tk()

varia = StringVar
mylabel = Label(root, text="Select Your Favourite Programming Language", justify=CENTER)
mylabel.pack()

radio1 = Radiobutton(root, text="JavaScript", variable="varia", value="1", ).pack()
radio2 = Radiobutton(root, text="Python", variable="varia", value="2", ).pack()
radio3 = Radiobutton(root, text="C++", variable="varia", value="3", ).pack()
radio4 = Radiobutton(root, text="Java", variable="varia", value="4", ).pack()


root.mainloop()
