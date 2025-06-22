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
        
        
# class user:
#     pass

# class join(admin,user):
#     pass

obj = admin()

obj.add(1)
# for i,j in enumerate(d,1):
