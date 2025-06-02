# FASHION STORE

d = {
    '1':{
        "product_name":"shirt",
        "product_color":"red",
        "rating":4.5
    },
    '2':{
        "product_name":"cargo pent",
        "product_color":"black",
        "rating":4
    },
    '3':{
        "product_name":"sadi",
        "product_color":"brown",
        "rating": 3.5
    }
}
menu = """
    WELLCOME TO DJ FASHION STORE
    
    1) admin
    2) user
    3) exit
"""

while True:
    print(menu)
    role = int(input("Enter your role :"))
    
    if role == 1:
        
        admin_manu = """
            press 1 for add product
            press 2 for view product
            press 3 for update product
            press 4 for delete product
            press 5 for exit
        """
        while True:
            print(admin_manu)
            choice = int(input("enter your choice :"))
        
            if choice == 1:
                print("WELLCOME BACK SIR !!")
                id = input("Enter product id :")
                name = input("Enter product name :")
                color = input("Enter product color :")
                star = input("Enter product star :")
                
                d[id] = {
                    "product_name":name,
                    "product_color":color,
                    "rating":star,
                }
                print("PRODUCT IS ADDED")
                
                
            elif choice == 2:
                print("ALL PRODUCTS")
                for i,n in d.items():
                    print(i, " :")
                    for key,value in n.items():
                        print(key,":",value)
                print("-------------------------")
                
                        
            elif choice == 3:
                id = input("Enter product id to update :")
                name = input("Enter product name :")
                color = input("Enter product color :")
                star = input("Enter product star :")
                
                d[id] = {
                    "product_name":name,
                    "product_color":color,
                    "rating":star,
                }
                
                print("PRODUCT IS UPGRADE")
            
            elif choice == 4:
                id = input("Enter product id to deleted :")
                d.pop(id)
                print("PRODUCT IS DELETED")
                        
            elif choice == 5:
                print("Thank you sir ")
                break
        
        
    elif role == 2:
        print("Wellcome ro shopping")
        
        
    elif role == 3:
        print("Thank you !")
        break
    
    else:
        print("Enter valid role")