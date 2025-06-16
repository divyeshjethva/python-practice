
class a:
    def fun1(self):
        super().fun1()
        print("method 1")

class b:
    def fun1(self):
        print("method 2")

class c(a,b):
    def fun1(self):
        super().fun1()
        print("method 3")

obj = c()
obj.fun1()