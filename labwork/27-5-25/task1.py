# finicobi series

n = 10
a = 0
b = 1
list1 = []

for i in range(1,n+1):
    list1.append(a)
    a, b = b, a+b

print(list1)
