# tuple 

t = (1,2,"hello","world",1,1,"world")

print(t.count("world"))
print(t.count(1))
print(t.index(2))

l1 = list(t)
print(l1)
l1.append("wellcome")
# print(l1)
print(tuple(l1))

# t1 = tuple(l1)
# print(t1)


# for i in t:
#     print(i)