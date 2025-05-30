

a = [
    {
        "name" : "divyesh",
        "marks" : 78,
        "cource" : "BCA"
    },
    {
        "name" : "ajay",
        "marks" : 78,
        "cource" : "BCA"
    },
    {
        "name" : "umang",
        "marks" : 78,
        "cource" : "BCA"
    }
]

for i in a:
    # print(i)
    for j,n in i.items():
        print(j , n)
    print("----------------")
    
#-----------------------------------------
    
# while True:

#     name = input("Enter name :")
#     mark = input("Enter mark :")
#     cource = input("Enter cource :")

#     d = {
#         "name" : name,
#         "mark" : mark,
#         "cource" : cource
#     }

#     print(d)
#     a.append(d)
#     print(a)

    # for i,j in d.items():
    #     print(i,j)