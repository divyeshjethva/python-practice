students = {
    "name" : "divyesh",
    "age" : 20,
    "role" : "Backend developer"
}

print(students.items())

print(students.get("name"))
print(students.get("age"))
print(students.get("role"))
students.pop("age")
students.update({"salary":15000})
print(students.get("salary"))

print(students)

keys = (1,2,3)
values = ("hello","world","wellcome")
d1 ={}
a = d1.fromkeys(keys,values)

print(a)


