class myclass1:
    def student(self):
        name = input("Enter name :")
        roll = input("Enter role no. :")
        
        print(name,roll)
        
class myclass2(myclass1):
    def marks(self):
        guj = int(input("Enter guj marks :"))
        eng = int(input("Enter eng marks :"))
        hin = int(input("Enter hin marks :"))
        
        p = guj + eng + hin 
        marks = (p/300)*100
        print(marks)
        
        if marks >= 80 and marks <= 100:
            print("First class")
        elif marks >= 50:
            print("second class")
        elif marks >=25 and marks <= 50:
            print("pass")
        elif marks <= 33:
            print("fail")
        else:
            print("invalid marks")
            

obj = myclass2()
obj.student()
obj.marks()
