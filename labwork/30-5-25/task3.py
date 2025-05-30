# student marks record

nameA = []
marksA = []

student_number = int(input("Enter number of student :")) 

for i in range(1,student_number+1):
    name = input("student name :")
    marks = int(input("student marks :"))
    nameA.append(name)
    marksA.append(marks)

print(nameA,marksA)