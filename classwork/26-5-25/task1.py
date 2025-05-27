# string

def centerName(name):
    s1 = int(len(name)/2)
    
    if len(name)%s1==0:
        print(name,"is a even string and enter a odd string ")
    else:
        print(name[s1-1],name[s1],name[s1+1])
    
name = input("Enter name :")
centerName(name)
