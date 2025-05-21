
def factorial(user):
    fact = 1
    for i in range(1,user+1):
        fact*=i
    print(user,"is factorial :", fact)    
    
def checkprime(user):
    prime = 0
    for i in range(1,user+1):
        if user%i==0:
            prime+=1
    
    if prime==2:
        print(user, "prime number")
    else:
        print(user, "not prime number")
    
def triangle(user):
    
    for i in range(1, user+1):
        print(" "*(user-i) + " *"*i)
    
        
    

def menuDriveen():
    menu = """
        press 1 to check factorial number
        press 2 to check prime number
        press 3 to print triangle number
        press 4 to exit
    """
    
    while True:
        print(menu)
        
        choice = int(input("press Number to check oparations :"))
        
        if choice == 1:
            user = int(input("find factorial number :"))    
            factorial(user)
        
        elif choice == 2:
            user = int(input("check prime number :"))
            checkprime(user)
        
        elif choice == 3:
            user = int(input("print a triangle:"))
            triangle(user)
        
        elif choice == 4:
            print("Thank you !!")
            break
        
        else:
            print("press valid number")
        
        
menuDriveen()
