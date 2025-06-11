import tkinter as tk
from tkinter import messagebox
import random
import os

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.c_name = tk.StringVar()
        self.c_phone = tk.StringVar()
        self.bill_no = tk.StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        # Product variables
        self.cosmetics = {"Bath Soap": [tk.StringVar(), 40],
                          "Face Cream": [tk.StringVar(), 120],
                          "Face Wash": [tk.StringVar(), 140],
                          "Hair Spray": [tk.StringVar(), 180],
                          "Body Lotion": [tk.StringVar(), 260]}

        self.grocery = {"Rice": [tk.StringVar(), 80],
                        "Food Oil": [tk.StringVar(), 180],
                        "Daal": [tk.StringVar(), 130],
                        "Wheat": [tk.StringVar(), 240],
                        "Sugar": [tk.StringVar(), 170]}

        self.others = {"Maza": [tk.StringVar(), 60],
                       "Coke": [tk.StringVar(), 60],
                       "Frooti": [tk.StringVar(), 50],
                       "Nimkos": [tk.StringVar(), 20],
                       "Biscuits": [tk.StringVar(), 100]}

        for category in [self.cosmetics, self.grocery, self.others]:
            for item in category:
                category[item][0].set("0")

        # ================= Customer Frame ====================
        customer_frame = tk.LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"), bg="lightblue", fg="black")
        customer_frame.place(x=0, y=0, relwidth=1)

        tk.Label(customer_frame, text="Customer Name", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        tk.Entry(customer_frame, textvariable=self.c_name, width=20, font="arial 13").grid(row=0, column=1, pady=5, padx=10)

        tk.Label(customer_frame, text="Phone No.", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        tk.Entry(customer_frame, textvariable=self.c_phone, width=20, font="arial 13").grid(row=0, column=3, pady=5, padx=10)

        tk.Label(customer_frame, text="Bill No.", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        tk.Entry(customer_frame, textvariable=self.bill_no, width=20, font="arial 13").grid(row=0, column=5, pady=5, padx=10)

        # ============== Products Frames ==================
        self.create_product_frame("Cosmetics", self.cosmetics, 0, 80)
        self.create_product_frame("Grocery", self.grocery, 340, 80)
        self.create_product_frame("Others", self.others, 680, 80)

        # ================= Bill Area =====================
        bill_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
        bill_frame.place(x=1020, y=80, width=330, height=400)
        tk.Label(bill_frame, text="Bill Area", font="arial 15 bold").pack(fill=tk.X)
        self.textarea = tk.Text(bill_frame)
        self.textarea.pack(fill=tk.BOTH, expand=1)

        # ================= Total Buttons =================
        btn_frame = tk.Frame(self.root, bd=7, relief=tk.GROOVE)
        btn_frame.place(x=0, y=580, relwidth=1, height=120)

        tk.Button(btn_frame, text="Total", command=self.total, bg="cadetblue", fg="white", pady=15, width=20, font="arial 12 bold").grid(row=0, column=0, padx=15, pady=20)
        tk.Button(btn_frame, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white", pady=15, width=20, font="arial 12 bold").grid(row=0, column=1, padx=15, pady=20)
        tk.Button(btn_frame, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15, width=20, font="arial 12 bold").grid(row=0, column=2, padx=15, pady=20)
        tk.Button(btn_frame, text="Exit", command=self.exit_app, bg="cadetblue", fg="white", pady=15, width=20, font="arial 12 bold").grid(row=0, column=3, padx=15, pady=20)

    def create_product_frame(self, title, products, x, y):
        frame = tk.LabelFrame(self.root, text=title, font=("times new roman", 15, "bold"), bg="lightyellow", fg="black")
        frame.place(x=x, y=y, width=330, height=400)
        for i, (item, (var, price)) in enumerate(products.items()):
            tk.Label(frame, text=f"{item}", font="arial 12 bold", bg="lightyellow").grid(row=i, column=0, padx=10, pady=10, sticky="w")
            tk.Entry(frame, textvariable=var, width=10).grid(row=i, column=1, padx=10, pady=10)

    def total(self):
        self.total_cosmetics = sum(int(qty.get()) * price for qty, price in self.cosmetics.values())
        self.total_grocery = sum(int(qty.get()) * price for qty, price in self.grocery.values())
        self.total_others = sum(int(qty.get()) * price for qty, price in self.others.values())

        self.tax_cosmetics = round(self.total_cosmetics * 0.05, 2)
        self.tax_grocery = round(self.total_grocery * 0.03, 2)
        self.tax_others = round(self.total_others * 0.04, 2)

        self.total_bill = self.total_cosmetics + self.tax_cosmetics + \
                          self.total_grocery + self.tax_grocery + \
                          self.total_others + self.tax_others

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are required")
            return

        self.textarea.delete('1.0', tk.END)
        self.textarea.insert(tk.END, f"Welcome To Hanan's Retail\n")
        self.textarea.insert(tk.END, f"Bill No.: {self.bill_no.get()}\n")
        self.textarea.insert(tk.END, f"Customer Name: {self.c_name.get()}\n")
        self.textarea.insert(tk.END, f"Phone No.: {self.c_phone.get()}\n")
        self.textarea.insert(tk.END, f"====================================\n")
        self.textarea.insert(tk.END, f"Products\tQty\tPrice\n")
        self.textarea.insert(tk.END, f"====================================\n")

        for category in [self.cosmetics, self.grocery, self.others]:
            for item, (var, price) in category.items():
                if int(var.get()) > 0:
                    self.textarea.insert(tk.END, f"{item}\t{var.get()}\t{int(var.get())*price}\n")

        self.textarea.insert(tk.END, f"====================================\n")
        self.textarea.insert(tk.END, f"Total: Rs. {self.total_bill}\n")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op:
            bill_data = self.textarea.get('1.0', tk.END)
            with open(f"bills/bill_{self.bill_no.get()}.txt", "w") as f:
                f.write(bill_data)
            messagebox.showinfo("Saved", f"Bill No. {self.bill_no.get()} saved successfully")

    def clear_data(self):
        self.c_name.set("")
        self.c_phone.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        for category in [self.cosmetics, self.grocery, self.others]:
            for item in category:
                category[item][0].set("0")
        self.textarea.delete('1.0', tk.END)

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op:
            self.root.destroy()

if __name__ == '__main__':
    if not os.path.exists("bills"):
        os.makedirs("bills")
    root = tk.Tk()
    obj = BillingApp(root)
    root.mainloop()