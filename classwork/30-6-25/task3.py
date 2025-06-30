from tkinter import *
from task2 import *

def fun2():   
    root = Tk()

    root.geometry("500x500")
    root.title("wellcome sir")

    name = Label(root,text="Name :", font=('Arial',15,'bold'))
    name.place(x=50,y=50)
    
    mob = Label(root,text="Mobile no. :", font=('Arial',15,'bold'))
    mob.place(x=50,y=100)

    password = Label(root,text='password :',font=("Arial",15,'bold'))
    password.place(x=50,y=150)
    
    cpassword = Label(root,text='Confirm password :',font=("Arial",15,'bold'))
    cpassword.place(x=50,y=200)

    e_name = Entry(root,font=('Arial',12,'bold'))
    e_name.place(x=250,y=50)
    
    e_mob = Entry(root,font=('Arial',12,'bold'))
    e_mob.place(x=250,y=100)

    e_password = Entry(root,font=('Arial',12,'bold'))
    e_password.place(x=250,y=150)
    
    e_cpassword = Entry(root,font=('Arial',12,'bold'))
    e_cpassword.place(x=250,y=200)
    
    btn = Button(root,text='Register',font=('Arial',12,'bold'),bg='blue',fg='white', command=fun1)
    btn.place(x=200,y=280)
        
    root.mainloop()
