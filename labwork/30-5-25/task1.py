# login and sign up

import random

otp = random.randint(1001,9999)

d = {}
def signUp():
    name = input("Enter name :")
    email = input("Enter email :")
    mno = int(input("Enter mno :"))
    password = int(input("Enter password :"))
    cpassword = int(input("Enter cpassword :"))
    
    if password == cpassword:
        d["name"]=name
        d["email"]=email
        d["mno"]=mno
        d["password"]=password
        print("Registration succesfully")
    else:
        print("password and confirm password does'n match")
    print(d)

def login():
    print(d)
    email = input("Enter email :")
    password = int(input("Enter password :"))
    
    if email == d["email"] and password == d["password"]:
        print("login succesfully")
    else:
        print("Enter valid email and password")

def forgetPassword():
    mno = int(input("Enter mno :"))
    if mno == d["mno"]:
        print("Your OTP is :", otp)
        uotp = int(input("Enter your OTP :"))
        if otp==uotp:
            new = int(input("Enter new password :"))
            d["password"]=new
            print("password is update")
        else:
            print("Enter valid otp")
    else:
        print("invalid mobile number")
    print(d)

menu = """
    press 1 for sign up
    press 2 for login
    press 3 for forget password
    press 4 for exit
"""

while True:
    print(menu)
    
    choice = int(input("press number :"))
    
    if choice==1:
        signUp()
        
    elif choice==2:
        login()
        
    elif choice==3:
        forgetPassword()
        
    elif choice==4:
        print("Thank you !! ")
        break
    
    else:
        print("invalid number")