d = {
    "apple":{
        "qty":10,
        "price" : 100
    },
    "banana":{
        "qty":20,
        "price" : 00
    },
    "pine":{
        "qty":50,
        "price" : 500
    },
}

for i in d.keys():
    print(i)
    print("---------------------")
    
for j in d.values():
    print(j.items())
    for n in j.items():
        # print(n)
        for a in n:
            print(a)
    print("---------------------")
    
    # for j in i:
    #     # print(j)m
    #     print("---------------------")


# t = ('apple',{'qty':10, 'price':100})

# for i in t:
#     print(i)