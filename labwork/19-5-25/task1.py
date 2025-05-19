# check a prime number
n = int(input("Enter number :"))
prime = 0
for i in range(1,n+1):
    if n%i==0:
        prime+=1

if prime == 2:
    print(n, "is prime Number")
else:
    print(n, "not prime number")