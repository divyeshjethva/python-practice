import datetime

d ={}

class banker:
    def add(self):
        account_no = int(input("Enter account number :"))
        cname = input("Enter customer name :")
        balance = int(input("Enter opaning balance :"))
        time = datetime.datetime.now()
        
        d[account_no] = {
            "name": cname,
            "balance" : balance,
            "time": time
        }
        
        
    def view(self):
        for i,j in d.items():
            print(i,":")
            for k,v in j.items():
                print("  ",k,":",v)
        print("----------------------------")
    
    def search(self):
        account_no = int(input("Enter account number to search :"))
        for i,j in d.items():
            if i == account_no:
                for k,v in j.items():
                    print("  ",k,":",v)
            else:
                print("Account number is not find")

    
    def total_amount(self):
        sum = 0
        for i,j in d.items():
            for k,v in j.items():
                if k == "balance":
                    sum = sum + v
        print(sum)
    
class customer:
    def withdraw(self):
        print("WITHDROW MONEY")
        account_no = int(input("Enter account number:"))
        cwithdraw = int(input("Enter Amount to withdraw :"))
        
        for i,j in d.items():
            if i == account_no:
                for k,v in j.items():
                    if k == "balance":
                        if v >= cwithdraw:
                            debit = v - cwithdraw
                            print("withdraw successfull :",cwithdraw)
                            print("your total balance is :",debit)
                        else: 
                            print("infuse balance")
        
    def deposite(self):
        print("DEPOSITE MONEY")
        account_no = int(input("Enter account number:"))
        cdeposite = int(input("Enter Amount to deposite:"))
        
        for i,j in d.items():
            if i == account_no:
                for k,v in j.items():
                    if k == "balance":
                        credit = v + cdeposite
                        print("deposite successfull :",cdeposite)
                        print("your total balance is :",credit)
        
        
    def view_balance(self):
        account_no = int(input("Enter account number:"))
        for i,j in d.items():
            if i == account_no:
                for k,v in j.items():
                    print("Your balance is :", v)

    
class join(banker,customer):
    print("WELLCOME !")

obj = join()

while True:
    menu = """
        1. banker
        2. customer
        3. exit
    """
    print(menu)
    
    choice = int(input("Enter your choice :"))
    
    if choice == 1:
        print("WELLCOME BANK MANAGER")
        
        mmenu = """
            1. add customer
            2. view all customer
            3. search customer
            4. total balance
            5. exit
        """
        while True:
            print(mmenu)
            role = int(input("Enter to work oparation :"))
            
            if role == 1:
                obj.add()
                
            elif role == 2:
                obj.view()
                
            elif role == 3:
                obj.search()
            
            elif role == 4:
                obj.total_amount()
            
            else:
                print("thank you for oparation")
                break
                
    
    elif choice == 2:
        print("WELLCOME BACK CUSTOMER")
        cmanu = """
            1. withdrow
            2. deposite
            3. view balance
            4. exit
        """
        while True:
            print(cmanu)
            role = int(input("Enter to work oparation :"))
            if role == 1:
                obj.withdraw()
            elif role == 2:
                obj.deposite()
            elif role == 3:
                obj.view_balance()
            else:
                print("Thank you ")
                break
    
    else:
        print("Thank you")
        break


print("Thank you all")

