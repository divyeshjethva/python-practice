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

   
for j,n in d.items():
    print(j,":")
    for keys,value in n.items():
        print("     ",keys,":",value)
        
    print("---------------------")
