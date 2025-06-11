class first:
    def student(self):
        name = input("Enter name :")
        role = int(input("Enter role number :"))
        
        print(name , role)
    
class second(first):
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

obj = second()
obj.marks()