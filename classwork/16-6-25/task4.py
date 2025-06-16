# polimorphism

class a:
    def fun1(self):
        print("method 1")

class b(a):
    def fun1(self):
        super().fun1()
        print("method 2")

obj = b()
obj.fun1()