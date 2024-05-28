# Program to understant Entry widget and create a Login Form 



from tkinter import* 

def getvalue():

    print(f"Username is: {username.get()}")
    print(f"Password is: {password.get()}")


root = Tk()
root.geometry("880x580")
root.title("Login Form")

label1 = Label(root, text="Username")
label1.grid(row=0, column=0)
username = StringVar()

entry1 = Entry(root, textvariable=username)
entry1.grid(row=0, column=1)

label2 = Label(root, text="PassWord")
label2.grid(row=1, column=0)
password = StringVar()

entry2 = Entry(root, textvariable=password)
entry2.grid(row=1, column=1)

button1 = Button(root, text="Submit", command=getvalue)
button1.grid(row=2, column=0)


root.mainloop()