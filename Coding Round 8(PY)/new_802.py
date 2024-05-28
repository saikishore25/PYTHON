# Basic Geometry Methods 
# 1 pack()


from tkinter import*



root = Tk()       # This Tk() method creates a basic root window which we see in every application we use

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Hello Kishore")
myLabel3 = Label(root, text="Hello Sai", bg="blue")

myLabel4 = Label(root, text="Hello Varma")

myLabel1.pack(side = RIGHT)
myLabel2.pack(side = LEFT)           # Pack() is one way of arranging items in the tkinter
myLabel3.pack(side = TOP, fill=X)
myLabel4.pack(side = BOTTOM)

#fill attribute is used when the label needs to occupy complete place on any side of the part such as DIV in html 
#expand attribute is used with fill attribute so that they occupy given space properly 


# myLabel1.pack()
# myLabel2.pack()
# myLabel3.pack()
# myLabel4.pack()

root.mainloop()