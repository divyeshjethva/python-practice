def centerName():
    name = input("Enter name :")
    
    s1 = len(name)//2
    
    if len(name)%s1==0:
        print("Enter a even number")
    else:
        print(name[s1-1]+name[2]+name[s1+1])

def pelidrom():
    user = input("Enter to check pelidrom :")
    reverse_string = user[::-1]
    
    if user == reverse_string:
        print(user, "is pelidrom")
    else:
        print(user, "is not pelidrom")
        
def stringLenght():
    user = input("Enter to check lenght of string :")
    print(len(user))