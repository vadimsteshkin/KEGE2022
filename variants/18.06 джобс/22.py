for i in range(1,10000000):
    q=0
    x=i
    a=3*x+23
    b=3*x-17
    while a!=b and q<100:
        if a>b:a-=b
        else:b-=a
        q+=1
    if a==10:
        print(i)
        break