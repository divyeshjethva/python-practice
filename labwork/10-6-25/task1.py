li = []

menu = """
    1. add fruit
    2. view fruit
    3. update fruit
    4. exit
"""

while True:
    print(menu)
    
    try:
        choice = int(input("Enter your choice :"))  
        if choice == 1:
            name = input("Enter fruit name :")
            qty = int(input("Enter fruit qty :"))
            price = int(input("Enter fruit price :"))
        
            d = {
                "name":name,
                "qty":qty,
                "price":price
            }
            
            li.append(d)
    
        elif choice == 2:
            print("view fruit")
            
            for i in li:
                for j,n in i.items():
                    print(j,":",n)
                print("==========================")
        
        elif choice == 3:
            # name = input("Enter fruit name :")
            # qty = int(input("Enter fruit qty :"))
            # price = int(input("Enter fruit price :"))
            # d = {
            #     "name":name,
            #     "qty":qty,
            #     "price":price
            # }
            print("upadate product")
        
        elif choice == 4:
            print("Thank you")
            break
        else:
            print("invalid number")
    
    except:
        print("Enter num not string")