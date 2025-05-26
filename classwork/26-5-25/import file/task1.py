from task2 import *

menu = """
    press 1 for mid of string
    press 2 for pelidrom
    press 3 for lenght of string
    press 4 for exit 
    """

while True:
    print(menu)
    choice = int(input("Enter number :"))
    
    if choice == 1:
        centerName()
        
    elif choice == 2:
        pelidrom()
        
    elif choice == 3:
        stringLenght()
        
    elif choice == 4:
        print("Thank You !!")
        break
    
    else:
        print("Please press valid number")
        