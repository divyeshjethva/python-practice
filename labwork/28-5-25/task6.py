
# chat GPT questions

#==========================================
# Task 1: Odd-Even List Separator

# numbers = [10, 3, 5, 8, 12, 7, 9, 6]
# even = []
# odd = []

# for i in numbers:
#     if i%2==0:
#        even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)

#===========================================

# Task 2: String Character Counter

# user = "hello"
# d = {}

# for i in user:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
    
# print(d)

# ==========================================

#  Task 3: FizzBuzz (Logic building)
fizz = []
buzz = []
fizzbuzz = []
noAny = []

for i in range(1,101):
    if i%3==0:
        fizz.append(i)
    elif i%5==0:
        buzz.append(i)
    elif i%3==0 and i%5==0:
        fizzbuzz.append(i)
    else:
        noAny.append(i)
    
print(fizz)
print(buzz)
print(fizzbuzz)
print(noAny)