import random

otp = random.randint(1001,9999)

d = {}

menu = """
    press 1 for sign up
    press 2 for log in
    press 3 for forget password
    press 4 for exit
"""

while True:
    print(menu)
    choice = int(input("Enter number : "))
    
    if choice == 1:
        name = input("Enter name :")
        mno = int(input("Enter mobile number :"))
        email = input("Enter email :")
        password = int(input("Enter password :"))
        cpassword = int(input("Enter cpassword :"))
        
        if password == cpassword:
            d["name"] = name
            d["mno"] = mno
            d["email"] = email
            d["password"] = password
            print("registration successfully")
        else:
            print("password and c cpassword does not match")
    
        
    elif choice == 2:
        email = input("Enter email :")
        password = int(input("Enter password :"))
        
        if email == d["email"] and password == d["password"]:
            print("login succesfully")
        else:
            print("envalid password and")
        
        
    elif choice == 3:
        mno = int(input("Enter mobile number :"))
        
        if mno == d["mno"]:
            print("your otp is :", otp)
            uotp = int(input("Enter your otp"))
            if otp == uotp:
                npassword = int(input("Enter new password :"))
                d["password"]==npassword
                print("password is update")
            else:
                print("Enter valid otp ")
        else:
            print("mobile number does not match")

        
    elif choice == 4:
        print("thank you !!")
        break
    
    else:
        print("press valid number")