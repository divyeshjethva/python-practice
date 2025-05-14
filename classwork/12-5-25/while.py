
#1 to 10 print
# user = int(input("Enter Number :"))
# i = 1
# while i<=user:
#     print(i)
#     i=i+1

#============================================


# 10 to 1 print
# user = int(input("Enter Number :"))
# i = user
# while i>=0:
#     print(i)
#     i-=1 # i = i - 1

#===========================================

i = 1
n=1
even = 0
odd = 0
while i <= 5:
    n = int(input("Enter Number :"))
    print(n)
    if n%2==0:
        print("even")
        even += n
    else:
        print("odd")
        odd += n
    i+=1  # i = i + 1
print("even number sum :",even)
print("odd number sum :",odd)
print("Total sum of even or odd:", even + odd)