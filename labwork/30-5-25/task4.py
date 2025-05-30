# add a multiple student

num_student = int(input("Enter number of student :"))
d = {}
for i in range(1,num_student+1):
    name = input("Enter student name")
    mark = input("Enter student mark")
    d[name] = mark

print("student name and marks")
for name,mark in d.items():
    print(name ,": ", mark)