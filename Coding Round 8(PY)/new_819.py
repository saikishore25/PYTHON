# Program to understand Canvas in Python 

from tkinter import* 

root = Tk()

canvas_height = 400
canvas_width = 700

root.geometry(f"{canvas_width}x{canvas_height}")

canvas1 = Canvas(root, width=canvas_width, height=canvas_height)
canvas1.pack()


# Creating a line 
# create_line(from(x1,y1) to (x2,y2))

canvas1.create_line(0,65,104,560, fill="red")


# Creating a Rectangle 
# create_rectangle(topleftcoordinates(x1,y1), bottomrightcoordinates(x2,y2))

canvas1.create_rectangle(5,54,90,154, fill="blue", outline="grey", width=5)


# Creating a text 
# create_text(coordinatesofcentre of text(x1,y1), text)

canvas1.create_text(56,44, text="Tkinter Library")


# Creating an Oval 
# create_oval(topleftcoordinates(x1,y1), bottomrightcoordinates(x2,y2)) 
# It creates an oval inside a rectangle 

canvas1.create_oval(5,10,54,32)


# Creating a Polygon 
# create_polygon(coordinates)

canvas1.create_polygon(0,50,34,25, fill="orange")









root.mainloop()