for _ in range(1,100000):
    s=_
    n=1
    while s<=80:
        s+=7
        n*=3
    if n==81:
        print(_)