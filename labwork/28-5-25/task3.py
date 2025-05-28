list1 = [1,2,3,1,2,3,4,5,1]
uniqe = []
copys = []

for i in list1:
    if i not in uniqe:
        uniqe.append(i)
    else:
        copys.append(i)
        

print(list1)
print(uniqe)
print(copys)