for i in range(1000):
    d=i
    n=8
    s=6
    while s<=1800:
        s+=d
        n+=7
    if n==246:
        print(i)