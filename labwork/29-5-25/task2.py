student = []

for i in range(1,3):
    name = input("Enter student name :")
    marks = int(input("Enter student marks :"))
    
    if marks >=90:
        grade = "A"
    elif marks >=80:
        grade = "B"
    elif marks >=70:
        grade = "C"
    elif marks >=33:
        grade = "D"
    elif marks <33:
        grade = "fail"
    else:
        print("Enter valid marks ")
        
    d = {
        "name" : name, 
        "marks" : marks, 
        "grade" : grade, 
    }
    student.append(d)

for i in student:
    print("--------------------")
    print("name : ",i["name"])
    print("marks : ",i["marks"])
    print("grade : ",i["grade"])