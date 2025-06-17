# d = {"a":100,"b":200,"c":300}

# # print(d["b"])

# for k,v in d.items():
#     print(j)

d = {"p":1100,"q":1800}
d1 = {"r":800,"s":600}

# d.update(d1)
# print(d)

# for k,y in d1.items():
#     print(k,":",y*2)

for i,j in d1.items():
    d.update({i:j*2})
print(d)