d = {}
class admin:
    def add(self):
        name = input("Enter product name :")
        price = int(input("Enter product price :"))
        qty = int(input("Enter product qty"))
        d[name] = {"name":name, "price":price,"qty":qty}
        
    def view(self):
        for i,j in d.items():
            print(i,":")
            for k,v in j.items():
                print(k,":",v)
                
    def update(self):        
        name = input("Enter product name :")
        price = int(input("Enter product price :"))
        qty = int(input("Enter product qty"))
        d[name] = {"name":name, "price":price,"qty":qty}

obj = admin()

while True:
    menu = """
        press 1 for admin
        press 2 for user update
        press 3 for exit view
    """
    
    print(menu)
    choice = int(input("enter your choice :"))
    if choice == 1:
        obj.add()
    elif choice == 2:
        obj.update()
    elif choice == 3:
        obj.view()