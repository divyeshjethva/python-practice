from tkinter import *
from connection import *

def success(name):
    cursor.execute(f"INSERT INTO todo (name) VALUES ('{name}')")
    connection.commit()
    root = Tk()
    root.geometry("200x50")
    root.title("TODO LIST view all")

    view = Label(root,text='Successfully added',font=('Arial',15,'bold'))
    view.pack()

    root.mainloop()