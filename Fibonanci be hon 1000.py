a,b=0,1
total=0
print(a,end=" ")
while (b<=1000-1):
    total += a
    a,b = b, a+b
    print(a,end=" ")