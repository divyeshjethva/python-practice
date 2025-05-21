# Fibonacci Series Generator

def fibonacci(n):
    a = 0
    b = 1
    sum = []
    for i in range(n):
        sum.append(a)
        a,b = b,a+b
    print(sum)
    

fibonacci(6)    