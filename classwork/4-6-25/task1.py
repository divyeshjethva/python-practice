
# even = []
# odd = []
# for i in range(1,6):
#     n = int(input("Enter number :"))
#     if n%2==0:
#         even.append(n)
#     else:
#         odd.append(n)

# print(even)
# print(odd)

#============================================

# l = []
# def finocobbi(n):
#     a = 0
#     b = 1
    
#     for i in range(1,n+1):
#         l.append(a)
#         a,b = b,a+b
        
        
# n = int(input("Enter number"))
# finocobbi(n)

# print(l)

#============================================

# i = 1
# fact = 1
# while i<=4:
#     fact *= i
#     i+=1

# print(fact)

#============================================

# for i in range(1,6):
#     print(" " * i +" *"*(6-i))

#============================================

# user = input("Enter name :")

# reverse_string = user[::-1]

# if user == reverse_string:
#     print("it pelidrom")
# else:
#     print("not")

# =============================================

a1 = int(input("Enter number 1 : "))
a2 = int(input("Enter number 2 : "))
a3 = int(input("Enter number 3 : "))

if a1>a2 and a1>a3 :
        print(a1,"is gretest!")       
        
elif a2>a3:
    print(a2,"is gretest!")       

else:
 print(a3,"is gretest!")