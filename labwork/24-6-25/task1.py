d = {}
# Student Grade Management System

class student:
        
    def add(self,index):
        name = input("Enter student name :")
        roll = int(input("Enter student roll no. :"))
        print("ENTER MARKS :")
        guj = int(input("Gujrati :"))
        math = int(input("Maths :"))
        hin = int(input("Hindi :"))
        p = guj + math + hin
        
        print("total is :",p)
        print("persantage is :",p/3)
        a = p/3
        
        if a > 100:
            print("Enter valid marks")
            g = "not found"
        elif a <= 100 and a >= 90:
            g = "A"
        elif a < 90 and a >= 70:
            g = "B"
        elif a < 70 and a >= 33:
            g = "C"
        elif a < 33 and a >= 1:
            g = "FAIL"
        else:
            print("invalid marks")
        
        print("Grade is :",g)
        
        
        d[index] = {"student" : {"name":name,"roll no.":roll},"marks":{"gujrati":guj,"math":math,"hin":hin,"grade":g}}
    
        
    def upadte(self):
        name = input("Enter student name :")
        roll = int(input("Enter student roll no. :"))
        print("ENTER MARKS :")
        guj = int(input("Gujrati :"))
        math = int(input("Maths :"))
        hin = int(input("Hindi :"))
        
        d[index] = {"student" : {"name":name,"roll no.":roll},"marks":{"gujrati":guj,"math":math,"hin":hin}}
        
    def view(self):
        for a,b in d.items():
            print("ID :",a)
            for i,j in b.items():
                print("    ",i,":")
                for k,v in j.items():
                    print("        ",k,":",v)
            print("=====================")
                    
    def delete(self):
        id = int(input("Enter id to delete student :"))
        try:
            d.pop(id)
            print("Student Deleted successfully")
        except:
            print("Enter valid id")
obj = student()
index = 1
menu = """
    press 1 for add student
    press 2 for upadte student
    press 3 for view student
    press 4 for delete student
    press 5 for exit
"""

while True:
    print(menu)
    choice = int(input("Enter your choice :"))
    if choice == 1:
        obj.add(index)
        index += 1
    elif choice == 2:
        obj.upadte()
    elif choice == 3:
        obj.view()
    elif choice == 4:
        obj.delete()
    elif choice == 5:
        print("thank you !")
        break
    else:
        print("invalid number ")
    