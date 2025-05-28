l1 = []
user = int(input("Enter to print line :"))

for i in range(1,user+1):
    n1 = int(input("Enter number :"))
    l1.append(n1)

l1.sort()
print(l1)

print("smallest :", l1[0])
print("largest :", l1[-1])
print("second largest :", l1[-2])