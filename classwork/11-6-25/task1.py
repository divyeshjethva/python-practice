class myClass:
    def fun1(self, n):
        for i in range(1,n+1):
            print("*" * i)

class myClass2:
    def fun2(self):
        n = int(input("Enter number :"))
        for i in range(1,n+1):
            print(" "*(n-i+1) + " *"*i)
            
class myClass3:
    def fun3(self):
        print("Method 3!!")

obj = myClass()
obj.fun1(5)

obj = myClass2()
obj.fun2()

obj = myClass3()
obj.fun3()