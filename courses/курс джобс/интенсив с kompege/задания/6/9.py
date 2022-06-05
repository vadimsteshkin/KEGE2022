for i in range(1,10000):
    d=i
    n=1
    s=46
    while s<=2700:
        s+=d
        n+=4
    if n==121:
        print(i)
        break