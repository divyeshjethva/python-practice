li = [
    {
        "name":"ajay",
        "age":20
    },
    {
        "name":"umang",
        "age":50
    },
    {
        "name":"div",
        "age":25
    }
]

print(li)

for i in li:
    print(i)
    for k,v in i.items():
        print(k,":",v)
    print("==========================")