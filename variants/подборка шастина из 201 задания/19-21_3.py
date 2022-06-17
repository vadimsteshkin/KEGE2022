def f(a,b,c,m):
    if a+b>54:return c%2==m%2
    if c==m:return 0
    h=[f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if c%2!=m%2 else all(h)
for a in range(1,50):
    for m in range(5):
        if f(a,5,0,m):
            print(a,m)
            break