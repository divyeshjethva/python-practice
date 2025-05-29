employees = {
    1:{
        "name": "divyesh jethva",
        "age":20,
        "role": "Backend developer",
        "salary":50000
    },
    2:{
        "name": "ajay jethva",
        "age":21,
        "role": "frontend developer",
        "salary":30000
    },
    3:{
        "name": "dharmesh kamliya",
        "age":19,
        "role": "fullstack developer",
        "salary":40000
    },
    4:{
        "name": "jaypal rathod ",
        "age":19,
        "role": "MERN stack developer",
        "salary":25000
    },
    5:{
        "name": "umang gondhaniya",
        "age":19,
        "role": "Android developer",
        "salary":29000
    },
    6:{
        "name": "hardik jethva",
        "age":19,
        "role": "flutter developer",
        "salary":45000
    }
}

for i in employees:
    a = employees.get(i)
    print("------------------------")
    print(i)
    
    for j in a:
        print(a.get(j))
        
    if a.get("salary") >= 30000:
        print("this salary is higher")