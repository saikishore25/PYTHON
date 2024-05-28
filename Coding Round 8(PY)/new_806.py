# Program to implement input fields in Tkinter 

from tkinter import *

root = Tk()

mylabel = Label(root, text="Enter Your Name")
mylabel.pack()


myinput = Entry(root)
myinput.pack()

# It has many parameters same as label, button etc.
'''
1. bg
2. fg
3. state 
4. command
5. cursor
6. width 

'''
def myclick():

    mylabel2 = Label(root, text="Hello " + myinput.get())
    mylabel2.pack()



mybutton = Button(root, text="Submit", command=myclick)
mybutton.pack()



root.mainloop()

