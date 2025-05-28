d = {1:"hello", 2:"wellcome", 3:"hi"}
print(d.get(1))
print(d.items())
print(d.keys())
print(d.values())
d.update({4:"value",5:"right"})
print(d)
d.pop(1)
print(d)
d.popitem()
print(d)

t = (1,2,3,4)
d1 = {}
# print(d1.fromkeys(t))
print(d1.fromkeys(t,20))