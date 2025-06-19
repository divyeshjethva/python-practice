# encapulation

class my:
    def fun1(self):
        a = 10
        b = 20
        self.a = a
        self.b = b
        

class my1(my):
    def fun2(self):
        print(self.a + self.b)
        
obj = my1()
obj.fun1()
obj.fun2()