from tkinter import *
from connection import *
from success import *
from view import *

root = Tk()
root.geometry("500x500")
root.title("TODO LIST")

head = Label(root,text='TODO LIST',font=('Arial',22,'bold'))
head.place(x=150,y=50)

view = Button(root,text='view',font=('Arial',14,'bold'),command=view)
view.place(x=400,y=60)

e_entry = Entry(root,bg="yellow",font=('Arial',18,'bold'))
e_entry.place(x=90,y=200)

def handle():
    name = e_entry.get()
    success(name)

add = Button(root,text='Add',font=('Arial',13,'bold'),bg='blue',fg='white',command=handle)
add.place(x=380,y=200)
root.mainloop()