list1 = []

user = int(input("Enter number of line to print :"))

for i in range(1,user+1):
    n1 = int(input("Enter number :"))
    list1.append(n1)
    
list1.sort()
print(list1)

print("smallest number :",list1[0])
print("largest number :",list1[-1])
print("second largest number :",list1[-2])