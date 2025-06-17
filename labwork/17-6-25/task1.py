# test - 
menu = """
    1. uniqe list
    2. dictonary
    3. mid of string
    4. pyramid pettern
    5. exit
"""

while True:
    choice = int(input("Enter Your choice :"))
    
    if choice==1:
        l = [1,7,8,9,2,1,1,2]
    
    elif choice==2:
        d = {"p":1100,"q":1800}
        d1 = {"r":800,"s":600}

        # output : {"p":1100,"q":1800,"r":1600,"s":1200}
    
    elif choice == 3:
        print("mid of string")
    
    elif choice == 4:
        print("pyramid")
        n =5
        for i in range(1,n+1):
            print(" " * (n-i) + " *"*i)

        for j in range(1,n+1):
            print(" " * j+" *" * (n-j))
    
    else:
        print("Thank you")
        break

