class a:
    def fun1(self):
        print("method 1")

class b(a):
    def fun1(self):
        super().fun1()
        print("method 2")

class c(a):
    def fun1(self):
        super().fun1()
        print("method 3")

obj1 = b()
obj1.fun1()

obj2 = c()
obj2.fun1()