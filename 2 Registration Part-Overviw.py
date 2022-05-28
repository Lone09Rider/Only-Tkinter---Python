from tkinter import *

root = Tk()
root.title("Registration Form")
root.geometry("500x500")

def printt():
    print("Demo tkinter")

def exit1():
    exit()

l1 = Label(root, text="Registration Form", relief=SOLID, width=20, font=("times new roman", 19, "bold"), bg="gray", fg="white")
l1.place(x=90, y=53)

l2 = Label(root, text="First Name :", width=20, font=("times new roman", 10, "bold"))
l2.place(x=80, y=130)

l3 = Label(root, text="Last Name :", width=20, font=("times new roman", 10, "bold"))
l3.place(x=80, y=179)

b1 = Button(root, text="Login", width=12, fg='white', bg='brown', command=printt)
b1.place(x=150, y=380)

b2 = Button(root, text="Quit", width=12, fg='white', bg='brown', command=exit1)
b2.place(x=280, y=380)

root.mainloop()