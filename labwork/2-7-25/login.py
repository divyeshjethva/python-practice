from tkinter import *
from register import *
from main import *
from connection import *
from tkinter import messagebox

def login():   
    root = Tk()

    root.geometry("400x500")
    root.title("login page")

    head = Label(root,text="Login",font=("Arial",22,"bold"))
    head.pack()

    name = Label(root,text="Name :",font=('Arial',13,'bold'))
    name.place(x=40,y=70)
    e_name = Entry(root,font=('Arial',15))
    e_name.place(x=150,y=70)

    password = Label(root,text="Password :",font=('Arial',13,'bold'))
    password.place(x=40,y=130)
    e_password= Entry(root,font=('Arial',15))
    e_password.place(x=150,y=130)

    def mainHandle():
        name2 = e_name.get()
        password2 = e_password.get()
        cursor.execute(f"select * from users where name='{name2}' and password='{password2}'")
        data = cursor.fetchall()
        if data:
            # messagebox.showinfo("data is find")
            main(name2,password2)
        else:
            messagebox.showerror("data not found")
            

    btn = Button(root,text="Login",font=('Arial',15),fg='white',bg='blue',command=mainHandle)
    btn.place(x=150,y=220)
    
    new = Button(root,text='new user | Register now',bd=0,font=('Arial',11),fg='blue',command=register)
    new.place(x=100,y=270)

    root.mainloop()

login()