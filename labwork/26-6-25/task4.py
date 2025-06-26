# BANK MANAGEMENT SYSTEM

class user:
    def create(self):
        pass
    def deposit(self):
        pass
    def withdraw(self):
        pass
    def view(self):
        pass

obj = user()

menu = """
    press 1 for create account
    press 2 for deposite account
    press 3 for withdraw account
    press 4 for view account
    press 5 for exit
"""

while True:
    print(menu)
    choice = int(input("Enter your choice :"))
    
    if choice == 1:
        obj.create()
    elif choice == 2:
        obj.deposit()
    elif choice == 3:
        obj.withdraw()
    elif choice == 4:
        obj.view()
    elif choice == 5:
        print("Thank you !!")
        break
    else:
        print("invalid choice")