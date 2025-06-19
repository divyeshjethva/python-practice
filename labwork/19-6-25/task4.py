# polimorphism

# class a:
#     def fun1(self):
#         print("method 1")

# class b(a):
#     def fun1(self):
#         super().fun1()
#         print("method 2")
    
# obj = b()
# obj.fun1()

# ------------------------------------------------


class dada:
    def fun1(self):
        super().fun1()
        print("method 1")

class papa(dada):
    def fun1(self):
        super().fun1()
        print("method 2")

class mom:
    def fun1(self):
        print("methon 3")

class child(papa,mom):
    def fun1(self):
        super().fun1()
        print("method 4")
        
obj = child()
obj.fun1()