from task2 import *
# from task2 import sub
from task3 import *
# from task3 import div

first = int(input("Enter first number :"))
second = int(input("Enter second number :"))
oparation = input("Enter oparation :")

if oparation == "+":
    add(first,second)
    
elif oparation == "-":
    sub(first,second)
    
elif oparation == "*":
    mul(first,second)
    
elif oparation == "/":
    div(first,second)

else:
    print("Enter valid oparation")