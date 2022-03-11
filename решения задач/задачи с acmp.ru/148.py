i=input().split()
a,b=int(i[0]),int(i[1])
while a*b>0:
    if a>=b:a%=b
    else:b%=a
print(a+b)