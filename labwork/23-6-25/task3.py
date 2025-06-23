class admin:
    def add(self):
        pname = input("Enter product name :")
        price = input("Enter product price :")
        qty = input("Enter product qty :")

obj = admin()

while True:
    menu = """
        press 1 for admin
        press 2 for user
        press 3 for exit
    """
    print(menu)