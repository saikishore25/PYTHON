
from tkinter import * 

root = Tk()

root.title("NotePad")
root.geometry("550x200")

label1 = Label(text="Raise the Bar my Friend", bg="blue", fg="yellow", padx=44, pady=20, font=("comicsansms", 20, "bold"), bd = "8px", relief="raised", width=55  )
label1.pack(anchor="center", side="top", fill=NONE, expand=False)



root.mainloop()













"""
A. METHODS 

1. title() ----> Changes the title of the application 
2. geometry()  ----> It sets the initial dimensions of an application 


"""

"""
B. WIDGETS 

1. Label() ----> This is used to simply provide caption to other widgets, it can also hold images 
bg 
fg 
image 
relief 
height 
width 


"""