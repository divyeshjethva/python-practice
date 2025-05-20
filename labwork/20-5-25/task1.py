#functions 

def printTable():
    user = int(input("Enter number to print table :"))
    for i in range(1,11):
        print(user, "X", i, "=", user*i)
        
printTable()
