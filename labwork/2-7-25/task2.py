# from tkinter import *

# root = Tk()
# root.geometry("400x500")
# root.title("Home")

# lable = Label(root,text='hello',font=("Arial",15,'bold'),bg='red',fg='white')
# lable.pack()

# entry = Entry(root,font=("Arial",15,'bold'),bg='black',fg='white')
# entry.pack()

# frame = Frame(root, bg="white", width=100, height=100, bd=5)
# frame.pack(pady=20)

# def show_name():
#     print("work")

# btn = Button(root, text="Submit", command=show_name)
# btn.pack()

# root.mainloop()

# # ===================================================================

# #  Tkinter Layout System

# # pack
# from tkinter import *

# root = Tk()
# root.geometry("300x200")

# Label(root, text="Top").pack()
# Button(root, text="Click").pack()
# Entry(root).pack()

# # -----------------------------------------------
# # place

# Label(root, text="Username:").place(x=20, y=30)
# Entry(root).place(x=100, y=30)

# # -------------------------------------
# # Grid

# Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
# Entry(root, show="*").grid(row=1, column=1)

# root.mainloop()

# # ----------------------------------------------

# | Element      | Property Used                  | Effect                          |
# | ------------ | ------------------------------ | ------------------------------- |
# | Window BG    | `root.configure(bg="#f2f2f2")` | Light gray background           |
# | Fonts        | `font=("Arial", 12)`           | Clean modern fonts              |
# | Colors       | `bg`, `fg`, `activebackground` | Control button and label colors |
# | Entry Style  | `bd=2`, `relief="groove"`      | Adds subtle border to inputs    |
# | Button Style | `bg`, `fg`, `relief`, `bd`     | Adds color, depth, and border   |

# -------------------------------------------------
