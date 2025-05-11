# check a even or odd number

user = int(input("Enter value :"))

if user % 2 == 0:
    print("even number")
elif user % 2 != 0:
    print("odd number")
else:
    print("enter valid number")