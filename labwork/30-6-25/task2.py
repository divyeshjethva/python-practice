from tkinter import *

def fun1():
    # from task1 import e_name,e_password

    # name = e_name.get()
    # password = e_password.get()
    # # print(name,password)
    
    root = Tk()

    root.geometry("500x500")
    root.title("wellcome back sir")

    well = Label(root,text=f'WELLCOME SIR',font=('Arial',20,'bold'))
    well.pack()
    
    root.mainloop()
    