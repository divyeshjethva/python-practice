from tkinter import *
from task2 import *
from task3 import *

root = Tk()

root.geometry("500x500")
root.title("login page")

name = Label(root,text="Name :", font=('Arial',15,'bold'))
# name.pack()
name.place(x=50,y=50)
password = Label(root,text='password :',font=("Arial",15,'bold'))
password.place(x=50,y=100)

e_name = Entry(root,font=('Arial',12,'bold'))
e_name.place(x=170,y=50)

e_password = Entry(root,font=('Arial',12,'bold'),show='*')
e_password.place(x=170,y=100)

already = Label(root,text='Already Login ?')
already.place(x=140,y=140)

new = Button(root,text='New user', fg='blue', command=fun2)
new.place(x=230,y=140)

btn = Button(root,text='Login',font=('Arial',12,'bold'),fg='white',bg='blue', command=fun1)
btn.place(x=200,y=180)
root.mainloop()