class a:
    def fun1(self):
        super().fun1()
        
        a = 10
        b = 20
        self.a = a
        self.b = b

class b(a):
    def fun1(self):
        super().fun1()
        c = 30
        self.c = c
        
class c:
    def fun1(self):
        d = 40
        self.d = d

class d(b,c):
    def fun1(self):
        super().fun1()
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)

obj = d()
obj.fun1()