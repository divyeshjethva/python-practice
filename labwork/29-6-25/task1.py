# BANK MANAGEMENT SYSTEM
from connection import *

class user:
    def create(self):
        name = input("Enter name :")
        balance = int(input("Enter opaning balance :"))
        cursor.execute(f"INSERT INTO bank (name,balance) VALUES ('{name}',{balance})")
        print("Account created")
        connection.commit()
        cursor.execute(f"SELECT id FROM bank WHERE name='{name}'")
        a = cursor.fetchone()
        print("Your Account number is:",a[0])
        connection.commit()
        
    def deposit(self):
        no = int(input("Enter account no. to deposit :"))
        amount = int(input("Enter amount to deposit :"))
        cursor.execute(f"SELECT balance FROM bank WHERE id={no}")
        balance = cursor.fetchone()
        
        a = balance[0] + amount
        cursor.execute(f"UPDATE bank SET balance={a} WHERE id={no}")
        print("Deposit successfully")
        
        cursor.execute(f"SELECT balance FROM bank WHERE id={no}")
        bal2 = cursor.fetchone()
        print("your current balance is :",bal2[0])
        connection.commit()
            
    def withdraw(self):
        no = int(input("Enter account no. to withdraw :"))
        amount = int(input("Enter amount to deposit :"))
        cursor.execute(f"SELECT balance FROM bank WHERE id={no}")
        balance = cursor.fetchone()
        
        a = balance[0] - amount
        cursor.execute(f"UPDATE bank SET balance={a} WHERE id={no}")
        print("withdrow successfully")
        
        cursor.execute(f"SELECT balance FROM bank WHERE id={no}")
        bal2 = cursor.fetchone()
        print("your current balance is :",bal2[0])
        connection.commit()
    
    def view(self):
        cursor.execute("SELECT * FROM bank")
        data = cursor.fetchall()
        for i in data:
            # print(i)
            for j in i:
                print(j)
            print("==========")
        connection.commit()

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