l1 = []
evev = []
odd = []


for i in range(1,51):
    l1.append(i)
    if i%2==0:
        evev.append(i)
    else: 
        odd.append(i)
        
    
print(l1)
print(evev)
print(odd)