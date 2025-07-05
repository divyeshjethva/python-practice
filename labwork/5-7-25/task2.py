from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("1200x700")
root.title("Billing Software")
root.configure(bg="darkblue")

# ===== Variables =====
c_name = StringVar()
c_phone = StringVar()
bill_no = StringVar(value="2367")

cosmetics = {
    "Bath Soap": [StringVar(value="0"), 40],
    "Face Cream": [StringVar(value="0"), 120],
    "Face Wash": [StringVar(value="0"), 140],
    "Hair Spray": [StringVar(value="0"), 180],
    "Body Lotion": [StringVar(value="0"), 260]
}

grocery = {
    "Rice": [StringVar(value="0"), 80],
    "Food Oil": [StringVar(value="0"), 180],
    "Daal": [StringVar(value="0"), 130],
    "Wheat": [StringVar(value="0"), 240],
    "Sugar": [StringVar(value="0"), 170]
}

others = {
    "Maza": [StringVar(value="0"), 60],
    "Coke": [StringVar(value="0"), 60],
    "Frooti": [StringVar(value="0"), 50],
    "Nimkos": [StringVar(value="0"), 20],
    "Biscuits": [StringVar(value="0"), 100]
}

# ======= GUI Design ========

# Top Frame - Title
Label(root, text="Billing Software", font=("times new roman", 30, "bold"), fg="white", bg="darkblue").pack(fill=X)

# Customer Frame
cust_frame = LabelFrame(root, text="Customer Details", font=("times new roman", 15, "bold"), bg="cyan", bd=7, relief=GROOVE)
cust_frame.place(x=0, y=60, relwidth=1)

Label(cust_frame, text="Customer Name", bg="cyan", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=20, pady=5)
Entry(cust_frame, textvariable=c_name, width=20, font="arial 12").grid(row=0, column=1, padx=10)

Label(cust_frame, text="Phone No.", bg="cyan", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=20, pady=5)
Entry(cust_frame, textvariable=c_phone, width=20, font="arial 12").grid(row=0, column=3, padx=10)

Label(cust_frame, text="Bill No.", bg="cyan", font=("times new roman", 12, "bold")).grid(row=0, column=4, padx=20, pady=5)
Entry(cust_frame, textvariable=bill_no, width=20, font="arial 12").grid(row=0, column=5, padx=10)

# Product Frame Function
def create_product_frame(title, items, x, y):
    frame = LabelFrame(root, text=title, font=("times new roman", 15, "bold"), bg="lightblue", bd=7, relief=GROOVE)
    frame.place(x=x, y=y, width=320, height=260)
    for i, (name, (var, _)) in enumerate(items.items()):
        Label(frame, text=name, font=("times new roman", 12, "bold"), bg="lightblue").grid(row=i, column=0, padx=10, pady=5, sticky="w")
        Entry(frame, textvariable=var, width=10).grid(row=i, column=1, padx=10, pady=5)

create_product_frame("Cosmetics", cosmetics, 0, 130)
create_product_frame("Grocery", grocery, 320, 130)
create_product_frame("Others", others, 640, 130)

# ====== Bill Area ======
bill_frame = Frame(root, bd=7, relief=GROOVE)
bill_frame.place(x=960, y=130, width=230, height=400)
Label(bill_frame, text="Bill Area", font=("times new roman", 14, "bold")).pack(fill=X)
bill_text = Text(bill_frame, font="arial 10", bg="white")
bill_text.pack(fill=BOTH, expand=1)

# ===== Total and Tax Frame =====
def calc_total():
    tc = sum(int(q.get()) * p for q, p in cosmetics.values())
    tg = sum(int(q.get()) * p for q, p in grocery.values())
    to = sum(int(q.get()) * p for q, p in others.values())

    tax_c = round(tc * 0.05)
    tax_g = round(tg * 0.05)
    tax_o = round(to * 0.05)

    total_c.set(f"Rs. {tc}")
    total_g.set(f"Rs. {tg}")
    total_o.set(f"Rs. {to}")

    tax_c_var.set(f"Rs. {tax_c}")
    tax_g_var.set(f"Rs. {tax_g}")
    tax_o_var.set(f"Rs. {tax_o}")

    return tc + tg + to + tax_c + tax_g + tax_o

# Variables for totals and taxes
total_c = StringVar(value="Rs. 0")
total_g = StringVar(value="Rs. 0")
total_o = StringVar(value="Rs. 0")

tax_c_var = StringVar(value="Rs. 0")
tax_g_var = StringVar(value="Rs. 0")
tax_o_var = StringVar(value="Rs. 0")

total_frame = LabelFrame(root, text="Bill Menu", font=("times new roman", 15, "bold"), bg="white", bd=7, relief=GROOVE)
total_frame.place(x=0, y=390, relwidth=1, height=120)

Label(total_frame, text="Total Cosmetics", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5)
Entry(total_frame, textvariable=total_c, width=10).grid(row=0, column=1)

Label(total_frame, text="Total Grocery", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5)
Entry(total_frame, textvariable=total_g, width=10).grid(row=0, column=3)

Label(total_frame, text="Others Total", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=4, padx=10, pady=5)
Entry(total_frame, textvariable=total_o, width=10).grid(row=0, column=5)

Label(total_frame, text="Cosmetics Tax", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10)
Entry(total_frame, textvariable=tax_c_var, width=10).grid(row=1, column=1)

Label(total_frame, text="Grocery Tax", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2)
Entry(total_frame, textvariable=tax_g_var, width=10).grid(row=1, column=3)

Label(total_frame, text="Others Tax", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=4)
Entry(total_frame, textvariable=tax_o_var, width=10).grid(row=1, column=5)

# ====== Button Functions ======
def generate_bill():
    if not c_name.get() or not c_phone.get():
        messagebox.showerror("Error", "Enter customer details")
        return
    total_amt = calc_total()

    bill_text.delete('1.0', END)
    bill_text.insert(END, f"Welcome To Hanan's Retail\n")
    bill_text.insert(END, f"Bill No. : {bill_no.get()}\n")
    bill_text.insert(END, f"Customer : {c_name.get()}\n")
    bill_text.insert(END, f"Phone No : {c_phone.get()}\n")
    bill_text.insert(END, "-"*28 + "\n")
    bill_text.insert(END, "Product\tQty\tPrice\n")
    bill_text.insert(END, "-"*28 + "\n")

    for category in [cosmetics, grocery, others]:
        for item, (var, price) in category.items():
            qty = int(var.get())
            if qty > 0:
                bill_text.insert(END, f"{item}\t{qty}\t{qty*price}\n")

    bill_text.insert(END, "-"*28 + "\n")
    bill_text.insert(END, f"Total: Rs. {total_amt}\n")
    bill_text.insert(END, "-"*28 + "\n")

def clear_data():
    for cat in [cosmetics, grocery, others]:
        for var, _ in cat.values():
            var.set("0")
    c_name.set("")
    c_phone.set("")
    total_c.set("Rs. 0")
    total_g.set("Rs. 0")
    total_o.set("Rs. 0")
    tax_c_var.set("Rs. 0")
    tax_g_var.set("Rs. 0")
    tax_o_var.set("Rs. 0")
    bill_text.delete('1.0', END)

def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

# ====== Buttons ======
Button(total_frame, text="Total", command=calc_total, bg="blue", fg="white", font=("times new roman", 12, "bold"), width=15).grid(row=0, column=6, padx=10, pady=10)
Button(total_frame, text="Generate Bill", command=generate_bill, bg="green", fg="white", font=("times new roman", 12, "bold"), width=15).grid(row=1, column=6, padx=10, pady=10)
Button(total_frame, text="Clear", command=clear_data, bg="orange", fg="white", font=("times new roman", 12, "bold"), width=15).grid(row=0, column=7, padx=10, pady=10)
Button(total_frame, text="Exit", command=exit_app, bg="red", fg="white", font=("times new roman", 12, "bold"), width=15).grid(row=1, column=7, padx=10, pady=10)

root.mainloop()
