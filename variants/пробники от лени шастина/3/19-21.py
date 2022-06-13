def f(a,b,c,m):
    if a+b>76:return c%2==m%2
    if c==m:return 0
    h=[f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if c%2!=m%2 else all(h)
for i in range(70):
    for m in range(5):
        if f(7,i,0,m):
            print(i,m)
            break
