# menu bar

# prime number
# factorial number
# star pattern number

menu = """
    press 1 to find factorial
    press 2 to check prime number
    press 3 to triangle
    press 4 to exit
"""

while True:
    print(menu)
    choice = int(input("Enter number :"))
    
    if choice==1:
        user = int(input("find factorial number :"))
        fact = 1
        for i in range(1,user+1):
            fact*=i
        print(fact)
        
    elif choice==2:
        user = int(input("ckeck prime number :"))
        prime = 0
        for i in range(1,user+1):
            if user%i==0:
                prime+=1
        if prime==2:
            print(user, "is prime number")
        else:
            print(user, "in not prime number")
        
    elif choice==3:
        user = int(input("Enter to print triangle :"))
        for i in range(1,user+1):
            print(" "*(user-i) + " *"*i)
        
    elif choice==4:
        print("thank you")
        break
        
    else:
        print("press valid number !!")