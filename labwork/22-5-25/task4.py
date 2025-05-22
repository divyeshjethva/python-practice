# count vowels

def vowelsCount(n):
    vowels = "aeiou"
    add = 0
    for i in n:
        if i in vowels:
            add+=1
    
    print("Total vowels is :", add)
        
            
n = input("enter to count vowels string :")
vowelsCount(n)