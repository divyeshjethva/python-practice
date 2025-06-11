# multilevel inheritance

class myClass:
    def fun1(self, n):
        for i in range(1,n+1):
            print("*" * i)

class myClass2(myClass):
    def fun2(self):
        n = int(input("Enter number :"))
        for i in range(1,n+1):
            print(" "*(n-i+1) + " *"*i)
            

class myClass3(myClass2):
    def fun3(self):
        print("method 3")
            

obj = myClass3()
obj.fun1(5)
obj.fun2()
obj.fun3()