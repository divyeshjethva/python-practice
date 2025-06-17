l = [1,7,8,9,2,1,1,2]
# print(l.count(1))

li = []

for i in l:
    if l.count(i) > 1 and i not in li:
        li.append(i)

print(li) 
        
# l1 = []
# l2 = []

# for i in l:
#     if i in l1:
#         l2.append(i)
#     else:
#         l1.append(i)
    
# # print(l1)
# print(l2)