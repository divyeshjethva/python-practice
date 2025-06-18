class a:
    def fun1(self):
        a = 5
        self.a = a

class b(a):
    def fun2(self):
        print(self.a)
    
obj = b()
obj.fun1()
obj.fun2()