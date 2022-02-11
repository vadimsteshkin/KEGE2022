for i in range(100,100000):
    s=i
    s//=100
    n=1
    while s<51:
        s+=5
        n*=2
    if n==128:
        print(i)