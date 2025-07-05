from tkinter import *
from tkinter import messagebox
import datetime

class BillingApp:
    bill_counter = 1001  # Static bill number

    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.bill_no.set(str(BillingApp.bill_counter))

        # Product data
        self.cosmetics = {"Bath Soap": [StringVar(), 40],
                          "Face Cream": [StringVar(), 120],
                          "Face Wash": [StringVar(), 140],
                          "Hair Spray": [StringVar(), 180],
                          "Body Lotion": [StringVar(), 260]}

        self.grocery = {"Rice": [StringVar(), 80],
                        "Food Oil": [StringVar(), 180],
                        "Daal": [StringVar(), 130],
                        "Wheat": [StringVar(), 240],
                        "Sugar": [StringVar(), 170]}

        self.others = {"Maza": [StringVar(), 60],
                       "Coke": [StringVar(), 60],
                       "Frooti": [StringVar(), 50],
                       "Nimkos": [StringVar(), 20],
                       "Biscuits": [StringVar(), 100]}

        for category in [self.cosmetics, self.grocery, self.others]:
            for item in category:
                category[item][0].set("0")

        self.customer_frame()
        self.create_product_frame("Cosmetics", self.cosmetics, 0, 80)
        self.create_product_frame("Grocery", self.grocery, 340, 80)
        self.create_product_frame("Others", self.others, 680, 80)
        self.bill_area_frame()
        self.buttons_frame()

    def customer_frame(self):
        c_frame = LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"), bg="lightblue")
        c_frame.place(x=0, y=0, relwidth=1)

        Label(c_frame, text="Customer Name", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        Entry(c_frame, textvariable=self.c_name, width=20, font="arial 13").grid(row=0, column=1, pady=5, padx=10)

        Label(c_frame, text="Phone No.", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        Entry(c_frame, textvariable=self.c_phone, width=20, font="arial 13").grid(row=0, column=3, pady=5, padx=10)

        Label(c_frame, text="Bill No.", bg="lightblue", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        Entry(c_frame, textvariable=self.bill_no, width=20, font="arial 13", state='readonly').grid(row=0, column=5, pady=5, padx=10)

    def create_product_frame(self, title, products, x, y):
        frame = LabelFrame(self.root, text=title, font=("times new roman", 15, "bold"), bg="lightyellow")
        frame.place(x=x, y=y, width=330, height=400)
        for i, (item, (var, price)) in enumerate(products.items()):
            Label(frame, text=f"{item}", font="arial 12 bold", bg="lightyellow").grid(row=i, column=0, padx=10, pady=10, sticky="w")
            Entry(frame, textvariable=var, width=10).grid(row=i, column=1, padx=10, pady=10)

    def bill_area_frame(self):
        frame = Frame(self.root, bd=10, relief=GROOVE)
        frame.place(x=1020, y=80, width=330, height=400)
        Label(frame, text="Bill Area", font="arial 15 bold").pack(fill=X)
        self.textarea = Text(frame)
        self.textarea.pack(fill=BOTH, expand=1)

    def buttons_frame(self):
        btn_frame = Frame(self.root, bd=7, relief=GROOVE)
        btn_frame.place(x=0, y=580, relwidth=1, height=120)

        Button(btn_frame, text="Total", command=self.total, bg="cadetblue", fg="white", pady=15, width=20, font="arial 12 bold").grid(row=0, column=0, padx=15, pady=20)
        Button(btn_frame, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white", pady=15, width=20, font="arial 12 bold").grid(row=0, column=1, padx=15, pady=20)
        Button(btn_frame, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15, width=20, font="arial 12 bold").grid(row=0, column=2, padx=15, pady=20)
        Button(btn_frame, text="Exit", command=self.root.quit, bg="cadetblue", fg="white", pady=15, width=20, font="arial 12 bold").grid(row=0, column=3, padx=15, pady=20)

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

        self.textarea.delete('1.0', END)
        self.textarea.insert(END, f"Welcome To Hanan's Retail\n")
        self.textarea.insert(END, f"Bill No.: {self.bill_no.get()}\n")
        self.textarea.insert(END, f"Customer Name: {self.c_name.get()}\n")
        self.textarea.insert(END, f"Phone No.: {self.c_phone.get()}\n")
        self.textarea.insert(END, f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        self.textarea.insert(END, f"====================================\n")
        self.textarea.insert(END, f"Products\tQty\tPrice\n")
        self.textarea.insert(END, f"====================================\n")

        for category in [self.cosmetics, self.grocery, self.others]:
            for item, (var, price) in category.items():
                if int(var.get()) > 0:
                    self.textarea.insert(END, f"{item}\t{var.get()}\t{int(var.get())*price}\n")

        self.textarea.insert(END, f"====================================\n")
        self.textarea.insert(END, f"Total: Rs. {self.total_bill}\n")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op:
            bill_data = self.textarea.get('1.0', END)
            file_name = f"bill_{self.bill_no.get()}.txt"
            with open(file_name, "w") as f:
                f.write(bill_data)
            messagebox.showinfo("Saved", f"Bill No. {self.bill_no.get()} saved successfully")
            BillingApp.bill_counter += 1
            self.bill_no.set(str(BillingApp.bill_counter))

    def clear_data(self):
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set(str(BillingApp.bill_counter))
        for category in [self.cosmetics, self.grocery, self.others]:
            for item in category:
                category[item][0].set("0")
        self.textarea.delete('1.0', END)

root = Tk()
obj = BillingApp(root)
root.mainloop()
