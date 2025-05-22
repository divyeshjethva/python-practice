#armstrong number check

def armstrong(value):
    sum = 0
    for i in value:
        sum += int(i)*int(i)*int(i)
    
    if sum == int(value):
        print(value,"is armstrong number ")
    else:
        print(value,"is not armstrong number ")
        

value = input("check armstrong number :")
armstrong(value)