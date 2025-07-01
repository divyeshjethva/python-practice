from tkinter import *
from tkinter import messagebox

# Sample credentials
USERNAME = "admin"
PASSWORD = "1234"

def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if not user or not pwd:
        messagebox.showwarning("Warning", "Please fill in all fields.")
    elif user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login Success", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root = Tk()
root.title("Stylish Login Page")
root.geometry("400x500")
root.configure(bg="#f0f4f7")

Label(root, text="🔐 Login", font=("Arial Rounded MT Bold", 28), bg="#f0f4f7", fg="#333").pack(pady=40)

frame = Frame(root, bg="white", bd=2, relief=SOLID)
frame.pack(pady=10, padx=30)

Label(frame, text="Username", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, pady=10, padx=10, sticky="w")
entry_user = Entry(frame, font=("Arial", 12), width=25, bd=2, relief=GROOVE)
entry_user.grid(row=1, column=0, padx=10, pady=5)

# Password label and entry
Label(frame, text="Password", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, pady=10, padx=10, sticky="w")
entry_pass = Entry(frame, font=("Arial", 12), width=25, bd=2, relief=GROOVE, show="*")
entry_pass.grid(row=3, column=0, padx=10, pady=5)

# Login button
Button(root, text="Login", font=("Arial", 14, "bold"), bg="#007acc", fg="white", width=15, command=login).pack(pady=30)

# Footer
Label(root, text="© 2025 MyApp", font=("Arial", 9), bg="#f0f4f7", fg="#888").pack(side=BOTTOM, pady=10)

root.mainloop()
