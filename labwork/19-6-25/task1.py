class a:
    def fun1(self):
        a = 10
        b = 20
        self.a = a
        self.b = b

class b(a):
    def fun2(self):
        c = 30
        self.c = c
        
class c:
    def fun3(self):
        d = 40
        self.d = d

class d(b,c):
    def fun4(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)

obj = d()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()