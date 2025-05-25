def myFun(user):
    reverce_string = user[::-1]
    
    if reverce_string==user:
        return True
    else:
        return False

user = input("Enter to check screen :")
print(myFun(user))