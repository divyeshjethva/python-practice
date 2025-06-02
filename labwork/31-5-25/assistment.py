
d = {}
menu = """
    WELLCOME TO FRUIT MARKET 
    
    1) Manager
    2) Customer
"""

while True:
    print(menu)
    
    role = int(input("select your role :"))
    
    if role == 1:
        managerManu = """
            Fruit market manager
            
            1) add fruit stock
            2) view fruit stock
            3) update fruit stock
            4) exit
        """
        print(managerManu)
        
        while True:
            choice = int(input("Enter your choice :"))
            if choice == 1:
                print("ADD FRUIT STOCK")
                name = input("enter fruit name :")
                qty = int(input("enter qty (in kg) :"))
                price = int(input("enter fruit price :"))
                
                d[name] = {"qyt" : qty,"price" : price}
                print("fruit is added")
                
            elif choice == 2:
                # print(d)
                print("VIEW FRUIT STOCK")
                for j,n in d.items():
                    print(j,":")
                    for keys,value in n.items():
                        print("     ",keys,":",value)
                print("---------------------")
                
            elif choice == 3:
                name = input("Enter to fruit name to update :")
                qty = int(input("enter qty (in kg) :"))
                price = int(input("enter fruit price :"))
                
                d[name] = {"qty":qty,"price":price}
                
            elif choice == 4:
                print("Thank you manager")
                break
            
            else:
                print("press valid choice")
    
    elif role == 2:
        print("WELLCOME TO SHOPPING")
    
    elif role == 3:
        print("Thank you")
        break
    
    else:
        print("Enter valid role")   
            