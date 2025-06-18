d = {}
class manager:          
    def add(self):
        print("ADD PRODUCT")
        pname = input("Enter product name :")
        pqty = int(input("Enter product qty :"))
        pprice = int(input("Enter product price :"))
                
                
        d[pname] = {
            "QTY" : pqty,
            "PRICE" : pprice
        }
                
        total = pprice * pqty
                
        print("TOTAL INVESTMENT :", total)
        self.pname = pname
        self.pqty = pqty
        self.pprice = pprice
                
            
    def view(self):
        for k,v in d.items():
            print(k, " :")
            for i,j in v.items():
                print("    ",i,":",j)
            print("========================")
            
    def update(self):
        pname = input("Enter product name to update :")
        pqty = int(input("Enter product qty to update :"))
        pprice = int(input("Enter product price to update :"))
                
        d[pname] = {
            "QTY" : pqty,
            "PRICE" : pprice
        }
        print(d)
    
class coustemer(manager):
    def pus(self):
        print("BUY PRODUCT")
    
        cname = input("Enter product name to buy :")
        if cname == self.pname:
            cqty = int(input("Enter product qty :"))
            if self.pqty >= cqty:
                total = cqty * self.pprice
                plateform_charg = total * 0.10
                gst = total * 0.18
                net = total + plateform_charg + gst
                print("product price :",total)
                print("platform fees is :",plateform_charg)
                print("GST TAX is :",gst)
                print("TOTAL BILL is :",net)
                        
            else:
                print("qty availble is : ",self.pqty)
        else:
            print("PRODUCT IS NOT AVAILABLE")
                
obj = coustemer()
    
while True:
    menu = """
        1. manager
        2. coustmer
        3. exit
    """
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        
        while True:
            pmanu = """
                press 1 for add
                press 2 for view
                press 3 for update
                press 4 for exit
            """
            print(pmanu)
            role = int(input("Enter your manager choice :"))
            if role == 1:
                obj.add()
            elif role == 2:
                obj.view()
            elif role == 3:
                obj.update()
            else:
                print("Thank you manager")
                break
    elif choice == 2:
        obj.pus()
    
    else:
        print("Thank you !!")
        break