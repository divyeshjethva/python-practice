# Armstrong Number

def armstrong(n):
    sum = 0
    for i in n:
        sum+=int(i)*int(i)*int(i)
        
    if sum==int(n):
        print(n, "is armstrong number")
    else:
        print(n, "is not armstrong")
    

n = input("Enter number :")
armstrong(n)