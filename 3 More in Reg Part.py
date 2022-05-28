from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Registration Form")
root.geometry("500x500")

img = Image.open("C:/Users/KIRA/Desktop/Advanced Python Programming/Tkinter/Team Male.png")
photo = ImageTk.PhotoImage(img)

lab1 =Label(image=photo)
lab1.pack()

fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()


def printt():
    first = fn.get()
    sec = ln.get()
    dob1 = dob.get()
    var1 = var.get()
    print(f"Hello {first} {sec}")
    print(f"Your age is {dob}")
    print(f"You are from {var1}")

def exit1():
    exit()

l1 = Label(root, text="Registration Form", relief=SOLID, width=20, font=("times new roman", 19, "bold"), bg="gray", fg="white")
l1.place(x=90, y=110)

l2 = Label(root, text="First Name", width=20, font=("times new roman", 10, "bold"))
l2.place(x=80, y=180)

e1 = Entry(root, textvariable=fn)
e1.place(x=200, y=180)


l3 = Label(root, text="Last Name", width=20, font=("times new roman", 10, "bold"))
l3.place(x=80, y=229)

e2 = Entry(root, textvariable=ln)
e2.place(x=200, y=229)


l4 = Label(root, text="Age", width=20, font=("times new roman", 10, "bold"))
l4.place(x=80, y=278)
e3 = Entry(root, textvariable=dob)
e3.place(x=200, y=278)



l5 = Label(root, text="Country", width=20, font=("times new roman", 10, "bold"))
l5.place(x=80, y=327)

list1 = ["Nepal", "India", "Canada", "Bhutan"]
droplist = OptionMenu(root, var, *list1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=200, y = 327)



b1 = Button(root, text="Login", width=12, fg='white', bg='brown', command=printt)
b1.place(x=150, y=400)

b2 = Button(root, text="Quit", width=12, fg='white', bg='brown', command=exit1)
b2.place(x=280, y=400)

root.mainloop()