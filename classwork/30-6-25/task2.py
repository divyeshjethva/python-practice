from tkinter import *

def fun1():   
    root = Tk()

    root.geometry("500x500")
    root.title("wellcome back sir")

    well = Label(root,text='WELLCOME SIR',font=('Arial',20,'bold'))
    well.pack()
    
    root.mainloop()
    