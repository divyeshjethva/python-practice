from tkinter import *
from connection import *
from tkinter import ttk

def main(name,password):
    print(name,password)
    
    cursor.execute("select * from users")
    data = cursor.fetchall()
    
    root = Tk()
    root.geometry("400x500")
    root.title("main page")
    heading = Label(root,text=f'Wellome back {name} sir',font=('Arial',19,'bold'))
    heading.pack()
    
    
    columns = ("id", "name", "mobile", "password")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=60)

    # Insert data into treeview
    for row in data:
        tree.insert("", END, values=row)

    tree.pack(pady=20, fill=BOTH, expand=True)
    
    
    # for i in data:
    #     # print(i)
    #     id = Label(root,text=f'{i[0]}.',font=('Arial',9))
    #     id.place(x=50,y=60)
    #     name = Label(root,text=f'{i[1]}.',font=('Arial',9))
    #     name.pack()
    #     mobile = Label(root,text=f'{i[2]}.',font=('Arial',9))
    #     mobile.pack()
    #     password4 = Label(root,text=f'{i[3]}.',font=('Arial',9))
    #     password4.pack()

    root.mainloop()