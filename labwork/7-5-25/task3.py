val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
opartion = input("Enter second value: ")

if opartion=="+":
    print("add :", val1 + val2)
elif opartion=="-":
    print("sub :", val1 - val2)
elif opartion=="*":
    print("mul :", val1 * val2)
elif opartion=="/":
    print("div :", val1 / val2)
else :
    print("Enter valid opartion")