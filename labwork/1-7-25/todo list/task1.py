from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("TODO LIST")

head = Button(root,text='TODO LIST',font=('Arial',22,'bold'))
head.place(x=150,y=50)

view = Label(root,text='view',font=('Arial',14,'bold'))
view.place(x=400,y=60)

e_entry = Entry(root,bg="yellow",font=('Arial',18,'bold'))
e_entry.place(x=90,y=200)

add = Button(root,text='Add',font=('Arial',13,'bold'),bg='blue',fg='white')
add.place(x=380,y=200)
root.mainloop()