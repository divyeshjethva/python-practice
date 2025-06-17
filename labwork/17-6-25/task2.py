a = "divyesh"

odd = len(a) // 2

if odd%2 == 0:
    print("that is even string try")
else :
    # print("work")
    print( a[odd-1]+a[odd]+a[odd+1] )

print(odd)