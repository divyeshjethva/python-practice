
def sumNumber(a,b,oparation):
    if oparation=="+":
        print("add is: ", a+b)
    elif oparation=="-":
        print("sub is: ", a-b)
    elif oparation=="*":
        print("mul is: ", a*b)
    elif oparation=="/":
        print("div is: ", a/b)
    else:
        print("Enter valid number")


first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
oparation = input("Enter oparation +,-,*,/")

sumNumber(first,second,oparation)

