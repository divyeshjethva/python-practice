from tkinter import *
from connection import *

def view():
    root = Tk()
    root.geometry("500x500")
    root.title("TODO LIST view all")
    
    cursor.execute("SELECT * FROM todo")
    data = cursor.fetchall()
    connection.commit()

    for i in data:
        view = Label(root,text=f'name : {i[1]}',font=('Arial',20,'bold'))
        view.pack()
    connection.commit()
    root.mainloop()