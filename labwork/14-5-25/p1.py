i = 0

n = 100
while i <= n:
    i = int(input("Enter your expenses :"))
    print(i)
    n = n - i
    print(n)
    # i+=1

print(n)