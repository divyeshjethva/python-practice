
class a:
    def fun1(self):
        super().fun1()
        print("method 1")

class b:
    def fun1(self):
        super().fun1()
        print("method 2")

class c:
    def fun1(self):
        print("method 3")

class d(a,b,c):
    def fun1(self):
        super().fun1()
        print("method 4")

obj = d()
obj.fun1()