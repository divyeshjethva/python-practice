import datetime

l = []

menu = """
    Wellcome to E - Note
    
    press 1 for generate Note,
    press 2 for view Note,
    press 3 for Exit,
"""

while True:
    print(menu)
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        name = input("Enter E-note generater name :")
        if name.isdigit():
            print("INVALID NAME")
        else:
            title = input("Enter E-note title :")
            content = input("Enter E-note content :")
            time = datetime.datetime.now()
            d = {
                "Time": time,
                "GENERATOR NAME" : name,
                "E-NOTE Title" : title,
                "E-NOTE Description" : content,
            }
            l.append(d)
        
    elif choice == 2:
        print("ALL NOTE")
        for i in l:
            print("----------------------------")
            for key,value in i.items():
                print(key, " :", value)
            
    
    elif choice == 3:
        print("Thank you !!")
        break
    
    else:
        print("press valid number ")
        break

