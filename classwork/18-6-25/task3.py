class stock:
    def manager(self):
        print("wellcome")
        pname = input("Enter product name :")
        pqty = int(input("Enter product qty :"))
        pprice = int(input("Enter product price :"))
        
        total = pqty * pprice
        
        print("TOTAL PRODUCT BILL :", total)
        
        self.pname = pname
        self.pqty = pqty
        self.pprice = pprice
    
    def coustemer(self):
        print("Shopping ")
        cname = input("Enter product name :")
        if cname == self.pname:
            cqty = int(input("Enter product qty :"))
            if self.pqty > cqty:
                total = cqty * self.pprice
                print(total)
                increase = total * 0.10
                gst = total * 0.18
                net = total + increase + gst
                tax = net - total
                print("platform fees is :",tax)
                print("TAX is :",gst)
                print("total BILL is :",net)
                
            else:
                print("qty availble is : ",self.pqty)
        else:
            print("stock is not available")
            
        
    
obj = stock()
obj.manager()
obj.coustemer()