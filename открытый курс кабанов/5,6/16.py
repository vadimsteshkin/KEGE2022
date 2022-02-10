for _ in range(1,10000):
    n=1
    d=_
    while d//n>0:
        d-=2
        n+=3
    if n==46:
        print(_)
print(71+75)