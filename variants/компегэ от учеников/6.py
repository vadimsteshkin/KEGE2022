for _ in range(100000):
    s=_
    n=s//10+s%6
    while n<s:
        n+=5
        s+=4
    if n==1024:
        print(_)
