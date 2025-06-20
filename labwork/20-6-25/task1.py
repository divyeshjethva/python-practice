# find mid of String

# a = "dharmes"

# odd = len(a) // 2

# if odd%2 == 0:
#     print("Enter odd string")
# else:
#     print(a[odd-1] + a[odd] + a[odd+1])

# print(odd)

# ======================================================


# # Count vowels and consonants in a string - a,i,o,u,e

# vowels = 'aeiou'
# vowel_count = 0
# s = "divyeshee"

# for i in s:
#     if i in vowels:
#         vowel_count += 1
# print(vowel_count)

# =================================================

# pelidrom - wow,nayan

# s = "naya"

# rs = s[::-1]

# if rs == s:
#     print("pelidrom")
# else:
#     print("not")

# =======================================

# armstrong

# a = "20"
# b = 0
# for i in a:   
#     b += int(i) * int(i) * int(i)
    
# if b == int(a):
#     print("armstrong")
# else:
#     print("not")

# ========================================

# finanaci series

# a = 0 
# b = 1
# l = []

# for i in range(10):
#     l.append(a)
#     a,b = b, a+b
# print(l)

# ==============================================

# uniq list

# l = [1,2,3,1,2] 
# l1 = []
# l2 = []
# for i in l:
#     if i in l1:
#         l2.append(i)
#     else:
#         l1.append(i)
# print(l1)
# print(l2)


# =================================================

# convert to dictonary 

# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# d = {}

# for i in range(len(l1)):
#     d[l1[i]] = l2[i]
# print(d)

# =========================================

# charecter counter

# s = "ajay"
# d = {}
# for i in s:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)

# ================================================

# even or odd

# l1 = []
# l2 = []

# for i in range(1,5):
#     a = int(input("entr num:"))
#     if a%2==0:
#         l1.append(a)
#     else:
#         l2.append(a)
        
# print(l1)
# print(l2)