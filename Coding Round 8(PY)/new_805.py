# Program to explain button widget in tkinter 


from tkinter import*

root = Tk()       # This Tk() method creates a basic root window which we see in every application we use

def OnClick():

    myLabel = Label(root, text="This Worked Out")
    myLabel.pack() 


myButton = Button(root, text="Click Here", state=DISABLED, padx=5, pady=5, command=OnClick, relief=SUNKEN, bg="pink")  # This will create a clickable Button 

# There are various parameters even in button function 

myButton.pack()
 

root.mainloop()