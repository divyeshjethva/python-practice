# inheritance

# 1. single inheritance
# class a:
#     def fun1(self):
#         print("method 1")
# class b(a):
#     def fun2(self):
#         print("method 2")

# obj = b()
# obj.fun1()
# obj.fun2()


# 2. multilavel inheritance

# class a:
#     def fun1(self):
#         print("method 1")
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


# 3. multiple inheritance

# class a:
#     def fun1(self):
#         print("method 1")
# class b:
#     def fun2(self):
#         print("method 2")
# class c(a,b):
#     def fun3(self):
#         print("method 3")

# obj = c()
# obj.fun1()
# obj.fun2()
# obj.fun3()


# 4. hirache inheritance

# class a:
#     def fun1(self):
#         print("method 1")
# class b(a):
#     def fun2(self):
#         print("method 2")
# class c(a):
#     def fun3(self):
#         print("method 3")

# obj1 = b()
# obj2 = c()

# obj1.fun1()
# obj1.fun2()

# obj2.fun1()
# obj2.fun3()


# 5. hybrid inheritance

# class dada:
#     def fun1(self):
#         print("method 1")

# class papa(dada):
#     def fun2(self):
#         print("method 2")

# class mom:
#     def fun3(self):
#         print("methon 3")

# class child(papa,mom):
#     def fun4(self):
#         print("method 4")
        
# obj = child()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# obj.fun4()