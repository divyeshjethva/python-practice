from tkinter import *

root = Tk()
root.title("Simple Dropdown")
root.geometry("250x150")

choice = StringVar()
choice.set("Select Option")

options = ["Option 1", "Option 2", "Option 3"]

dropdown = OptionMenu(root, choice, *options)
dropdown.pack(pady=20)

def submit():
    Label(root, text="You selected: " + choice.get()).pack()

Button(root, text="Submit", command=submit).pack()

root.mainloop()
