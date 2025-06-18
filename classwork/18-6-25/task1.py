# encapsulation

class a:
    
    def fun1(self):
        self.a = 10
        self.b = 20
    
    def fun2(self):
        print(self.a)
        print(self.b)
        print(self.a + self.b)

obj = a()
obj.fun1()
obj.fun2()