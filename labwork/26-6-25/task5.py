d = {
    1:{
        "name": "ajay",
        "balance": 2000
    },
    2:{
        "name": "div",
        "balance": 1000
    },
    3:{
        "name": "umang",
        "balance": 5000
    }
}

while True:
    manu = """
        1. deposit
        2. withdrow
        3. view
    """
    print(manu)
    choice = int(input("Enter choice :"))
    if choice == 1:
        acc = int(input("Enter account num :"))
        for j,i in d.items():
            print(j,":")
            if acc == j:
                amount = int(input("Enter amount deposit :"))
                d[i["balance"]]
    elif choice == 2:
        pass
    elif choice == 3:
        for j,i in d.items():
            print(j,":",i)

