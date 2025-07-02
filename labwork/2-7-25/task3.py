from tkinter import *

root = Tk()
root.geometry("200x150")

var = StringVar()
var.set("Choose")

options = ["One", "Two", "Three"]
menu = OptionMenu(root, var, *options)
menu.pack(pady=20)

root.mainloop()
