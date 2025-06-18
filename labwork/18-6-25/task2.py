import datetime

l = []

class notebook:
    def generate_note(self):
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
            print("NOTE CREATE SUCCESFULLY")
    
    def view_note(self):
        print("ALL NOTE")
        for i in l:
            print("----------------------------")
            for key,value in i.items():
                print(key, " :", value)
    
obj = notebook()

while True:
    menu = """
        Wellcome to E - Note
        
        press 1 for generate Note,
        press 2 for view Note,
        press 3 for Exit,
    """
    print(menu)
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        obj.generate_note()
        
    elif choice == 2:
        obj.view_note()
        
    elif choice == 3:
        print("Thank you !!")
        break
    
    else:
        print("press valid number ")
        break