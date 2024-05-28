# Program to understand few basic methods in Tkinter Module 


from tkinter import* 
from PIL import Image, ImageTk

def updatedate():
    myLabel3.configure(text="This is updated")      # This Configure method is used to change data dynamically after a click 


root = Tk()
root.title("Note Pad")    # This gives the name of the Application 

# geomtry(height x width + shift towards X-axis + shift towards Y-axis)

root.geometry("440x550+800+400")      # This creates the default width and height of the application when clicked to open

#minsize(width, height)
# root.minsize(200,100)       # This sets the minimum width and height an application should definetly have
# root.maxsize(500,400)       # This sets the maximum width and height an application should definetly have

myLabel3 = Label(root, text="Hello Sai", bg="blue")
button3 = Button(root, text="Click Here", command=updatedate)
button3.pack()


root.mainloop()
