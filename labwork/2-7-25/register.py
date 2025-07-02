from tkinter import *
from main import *


def register():
    root = Tk()

    root.geometry("400x500")
    root.title("register page")

    head = Label(root,text="Register",font=("Arial",22,"bold"))
    head.pack()

    name = Label(root,text="Name :",font=('Arial',12,'bold'))
    name.place(x=40,y=70)
    e_name = Entry(root,font=('Arial',15))
    e_name.place(x=150,y=70)

    mob = Label(root,text="Mobile no :",font=('Arial',12,'bold'))
    mob.place(x=40,y=130)
    e_mob = Entry(root,font=('Arial',15))
    e_mob.place(x=150,y=130)

    password = Label(root,text="Password :",font=('Arial',12,'bold'))
    password.place(x=40,y=190)
    e_password= Entry(root,font=('Arial',15),show='*')
    e_password.place(x=150,y=190)

    cpassword = Label(root,text="Confirm P:",font=('Arial',12,'bold'))
    cpassword.place(x=40,y=250)
    e_cpassword= Entry(root,font=('Arial',15),show='*')
    e_cpassword.place(x=150,y=250)
    
    def handler():
        name1 = e_name.get()
        mob1 = e_mob.get()
        password1 = e_password.get()
        cpassword1 = e_cpassword.get()
        if password1 == cpassword1:
            cursor.execute(f"insert into users (name,mobile,password) values('{name1}',{mob1},'{password1}')")
            connection.commit()
            main(name1,password1)
        else:
            print("password does't match")

    btn = Button(root,text="Register",font=('Arial',15),fg='white',bg='blue',command=handler)
    btn.place(x=150,y=310)

    root.mainloop()