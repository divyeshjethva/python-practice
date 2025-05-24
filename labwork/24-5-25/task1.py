# strings slicing


str = "Python Programing"

print(type(str))
print(len(str))
print(str.replace("P","R")) 
print(str.center(25,"*"))   # ****Python Programing**** esa print hoga
print(str.capitalize()) # first latter capital kar dega
print(str.casefold()) #lower me print karega
print(str.lower())
print(str.upper())  
print(str.find("thon")) # index find karke dega
print(str.index("n")) # index find karke dega
print(str.swapcase()) # uper ko lower or lower ko upper me convert kar dega
print(str.title()) # jo string hogi esi same kar dega
print(str.strip()) # left or right se space ko nikal dega