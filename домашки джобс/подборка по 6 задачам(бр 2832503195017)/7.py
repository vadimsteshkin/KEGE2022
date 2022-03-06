for k in range(1000):
    s=k
    n=1
    while s<47:
        s+=4
        n*=2
    if n==64:
        print(k)