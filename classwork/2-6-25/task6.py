d = {}
d1 = {}
d3 = {}
def dictonary_sum():
    dic_manu = """
        press 1 for add dictonary
        press 2 for add second dictonary
        press 3 for view dictonary
        press 4 for sum for same dictonary
        press 5 for exit
    """
    while True:
        print(dic_manu)
        cho = int(input("Enter number :"))
        if cho == 1:
            # print("w")
            keys = input("Enter keys :")
            value = input("Enter value :")
            d[keys] = value
        elif cho == 2:
            keys2 = input("Enter keys2 :")
            value2 = input("Enter value2 :")
            d1[keys] = value
        elif cho == 3:
            
            for i,j in d.items():
                for k,l in d1.items():
                    if i == k:
                        d3[i]=j+l
                    else:
                        d3[i]=j
            print(d3)
            
        elif cho == 4:
            print(d3)
        elif cho == 5:
            print("thank you for exit")
            break
        else:
            print("Enter valid number")
    

menu = """
    press 1 for dictonary sum 
    press 2 for exit
"""

while True:
    print(menu)
    choice = int(input("Enter your choice :"))
    
    if choice == 1:
        # print("work")
        dictonary_sum()
        
    elif choice == 2:
        print("Thank you !")
        break
    else:
        print("Enter valid choice")