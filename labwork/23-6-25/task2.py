# l = {"a":1,"b":2,"c":3,"d":4}
# for i,j in enumerate(l,1):
#     print(j)
    
# ============================================

l = {"a":1,"b":2,"c":3,"d":4}
for i,(k,v) in enumerate(l.items(),1):
    print(i)
    print("key :", k, "value :",v)
    