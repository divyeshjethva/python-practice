from tkinter import *

root = Tk()
root.title("E-Commerce UI")
root.geometry("800x600")
root.configure(bg="#1fee1f")

# Heading
Label(root, text="🛍️ MyShop", font=("Arial Rounded MT Bold", 24), bg="#f9f9f9", fg="#333").pack(pady=20)

# Product Area Frame
product_area = Frame(root, bg="#f9f9f9")
product_area.pack(pady=10)

# Sample products (id, name, price)
products = [
    (1, "T-shirt", "₹499"),
    (2, "Jeans", "₹999"),
    (3, "Shoes", "₹1499"),
    (4, "Cap", "₹199"),
    (5, "Jacket", "₹1999"),
    (6, "Watch", "₹1299"),
]

# Create product cards in a grid (3 per row)
for i, product in enumerate(products):
    card = Frame(product_area, bd=2, relief="groove", bg="white", width=200, height=150)
    card.grid(row=i//3, column=i%3, padx=20, pady=20)

    Label(card, text=product[1], font=("Arial", 12, "bold"), bg="white").pack(pady=10)
    Label(card, text=product[2], font=("Arial", 10), bg="white", fg="green").pack()
    Button(card, text="Add to Cart", bg="#007acc", fg="white", font=("Arial", 10)).pack(pady=10)

root.mainloop()
