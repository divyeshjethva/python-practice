
user = input("Find a largest Number :")
# user = "512"
temp = 0
for i in user:
    print(i)
    if int(i) > temp:
        temp = int(i)

print("largest number is: ", temp)
