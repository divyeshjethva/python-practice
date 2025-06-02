d = {'p':120,'q':300,'r':800}
d1 = {'p':160,'q':800}
d3 = {}

# print(d1.keys())

for i,j in d.items():
    for k,l in d1.items():
        if i == k:
            d3[i]=j+l
        else:
            d3[i]=j

print(d3)