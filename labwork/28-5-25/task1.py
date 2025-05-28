list1 = []
even = []
odd = []

user = int(input("Enter number to add list :"))

for i in range(1,user+1):
    list1.append(i)
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print(list1)
print(even)
print(odd)