from tkinter import *
from connection import *

def fun1(name,mobile,password):
    # print(name,password)
    
    root = Tk()

    root.geometry("500x500")
    root.title("wellcome page")

    well = Label(root,text=f'WELLCOME {name} SIR',font=('Arial',20,'bold'))
    well.pack()
    
    cursor.execute(f"INSERT INTO tkinter (name, mobile, password) VALUES ('{name}',{mobile},'{password}')")
    connection.commit()
    
    root.mainloop()
    