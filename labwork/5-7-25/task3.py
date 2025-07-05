from tkinter import *

root = Tk()
root.geometry("1300x650")
root.title("Billing softwere")
root.configure(bg="#074463")

heading = Frame(root,height=80,width=1298,highlightbackground="black",bg="#074463",highlightthickness=4)
heading.pack()

Label(root,text="Billing software",font=('Arial',25,'bold'),fg='white',bg="#074463").place(x=500,y=15)

Frame(root,height=100,width=1298,highlightbackground="black",bg="#074463",highlightthickness=4).place(x=0,y=90)
Label(root,text='customer details',font=('Arial',15),bg="#074463",fg="yellow").place(x=10,y=80)
Label(root,text='Customer Name :',font=('Arial',16,'bold'),bg="#074463",fg='white').place(x=10,y=125)
Entry(root).place(x=200,y=128,height=24)

Label(root,text='Phone No. :',font=('Arial',16,'bold'),bg="#074463",fg='white').place(x=400,y=125)
Entry(root).place(x=530,y=128,height=24)

Label(root,text='Bill No. :',font=('Arial',16,'bold'),bg="#074463",fg='white').place(x=730,y=125)
Entry(root).place(x=820,y=128,height=24)

Frame(root,height=350,width=290,highlightbackground="black",bg="#074463",highlightthickness=4).place(x=1,y=199)
Label(root,text='costmetic',font=('Arial',15),bg="#074463",fg="yellow").place(x=10,y=190)



root.mainloop()

