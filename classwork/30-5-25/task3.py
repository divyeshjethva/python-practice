# guess number game
import random
original = random.randint(1,50)

while True:
    print("************ Enter Between 1 to 50 *************")
    
    choice = int(input("Enter number"))
    
    if choice>50:
        print("invalid number")
    
    elif choice==original:
        print("WIN !!")
        
    elif choice<original:
        print("that is bigger")
    
    else :
        print("that is smaller")

        