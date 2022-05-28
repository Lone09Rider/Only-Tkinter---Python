from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")

# Types of packing
# 1
# l1 = Label(window, fg="blue", bg="yellow", text="Welcome to Tkinter", font=("arial", 16, "bold"), relief=SOLID, borderwidth=5).place(x=110, y=110)

# 2
# Label(window, fg="blue", bg="yellow", text="Welcome to Tkinter", font=("arial", 16, "bold"), relief=SOLID, borderwidth=5).pack(fill=BOTH, padx=2, pady=2, expand=True)

# 3
l1 = Label(window, fg="blue", bg="yellow", text="Welcome to Tkinter", font=("arial", 16, "bold"), relief=SOLID, borderwidth=5)
l1.grid(row=0, column=0, padx=50, pady=90, columnspan=2)

def greet():
    l1 = Label(window, text="Hello User!!!", font=("times new roman", 10, "bold"))
    l1.grid(row=2, column=0, columnspan=2)


button1 = Button(window, text="Submit", fg="white", bg="black", command=lambda: greet())
button1.grid(row=1, column=0)

button2 = Button(window, text="Quit", fg="white", bg="black", command=window.destroy)
button2.grid(row=1, column=1)

window.mainloop()
