# string

def centerName(name):
    s1 = len(name)//2
    
    if len(name)%s1==0:
        print("Enter a even number")
    else:
        print(name[s1-1]+name[s1]+name[s1+1])
    

name = input("Enter name :")
centerName(name)
