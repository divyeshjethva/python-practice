l = [1,2,3,1,2]
l1 = []
l2 = []

for i in l:
    print(i)
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)

print(l1)
print(l2)