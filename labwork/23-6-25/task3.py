class user:
    def see(self):
        print("work")
        
class admin(user):
    def add(self, index):
        pname = input("Enter product name :")
        price = input("Enter product price :")
        qty = input("Enter product qty :")
        
        d[index] = {"name":pname,"price":price,"qty":qty}
        
    def view(self):
        for i,j in d.items():
            print(i,":")
            for k,v in j.items():
                print(k,":",v)
        
obj = admin()
d = {}
index = 1
while True:
    menu = """
        press 1 for admin
        press 2 for user
        press 3 for exit
    """
    print(menu)
    choice = int(input("Enter your choice"))
    if choice == 1:
        amanu = """
            press 1 for add
            press 2 for view
            press 3 for exit
        """
        print(amanu)
        role = int(input("enter to perform task :"))
        if role == 1:
            obj.add(index)
            index += 1
        elif role == 2:
            obj.view()
        elif role == 3:
            print("thanks admin")
            break
        
    elif choice == 2:
        pass
    elif choice == 3:
        print("Thank you ")
        break
    else:
        print("INVALID CHOICE")
        