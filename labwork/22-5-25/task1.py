#fibonacci series

def myFun(n):
    a=0
    b=1
    sum = []
    
    for i in range(1,n+1):
        sum.append(a)
        a,b = b, a+b
    
    return sum

user = int(input("Enter number :"))
demo = myFun(user)

for i in demo:
    print(i, end=" ")