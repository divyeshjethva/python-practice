# BANK MANAGEMENT SYSTEM
from connection import *

d = {}

class user:
    def create(self,index):
        name = input("Enter name :")
        balance = int(input("Enter opaning balance :"))
        d[index] = {"name":name, "balance":balance}
        print("your account no .:",index)
        cursor.execute(f"INSERT INTO bank (name,balance) VALUES ('{name}',{balance})")
        print("Account created")
        connection.commit()
        
    def deposit(self):
        no = int(input("Enter account no. to deposit :"))
        name = ""
        if no in d:
            for i,j in d.items():
                if i == no:
                    for k,v in j.items():
                        # print(k,":",v)
                        if k == "name":
                            print(v)
                            name = v
                        if k == "balance":
                            dep = int(input("Enter amount to deposit :"))
                            a = v + dep
                            print("current balance is :",a)
                            d[i] = {"name":name, "balance":a}
                            print("Deposit sucessfully")
        else:
            print("invalid account number")
            
    def withdraw(self):
        no = int(input("Enter account no. to withdraw :"))
        name = ""
        if no in d:
            for i,j in d.items():
                if i == no:
                    for k,v in j.items():
                        # print(k,":",v)
                        if k == "name":
                            print(v)
                            name = v
                        
                        if k == "balance":
                            dep = int(input("Enter amount to withdrew :"))
                            a = v - dep
                            print("current balance is :",a)
                            d[i] = {"name":name, "balance":a}
                            print("withdrew sucessfully")
        else:
            print("invalid account number")
    
    # def view(self):
    #     no = int(input("Enter account no. to view :"))
    #     if no in d:
    #         for i,j in d.items():
    #             if i == no:
    #                 # print(j)
    #                 for k,v in j.items():
    #                     print(k,":",v)
    #     else:
    #         print("invalid account number")
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
index = 1

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
        obj.create(index)
        index += 1
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