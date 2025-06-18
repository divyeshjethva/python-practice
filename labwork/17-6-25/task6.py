#  1. Single Inheritance

# class a:
#     def fun1(self):
#         print("method 1 !!!")
        
# class b(a):
#     def fun2(self):
#         print("method 2 !!!")

# obj = b()
# obj.fun1()
# obj.fun2()

# ===========================================

# Multilevel Inheritance
# class a:
#     def fun1(self):
#         print("Method 1")

# class b(a):
#     def fun2(self):
#         print("method 2")

# class c(b):
#     def fun3(self):
#         print("method 3")

# obj = c()
# obj.fun1()
# obj.fun2()
# obj.fun3()

# ===========================================

# Multiple Inheritance

class father:
    def fun1(self):
        print("method 1")
    
class mother:
    def fun2(self):
        print("method 2")

class child(father,mother):
    def fun2():
        print("method 3")

obj = child()

# ===========================================

# ===========================================

# ===========================================




