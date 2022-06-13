def f(a,b,c,m):
    if a+b>210:return c%2==m%2
    if c==m:return 0
    h=[f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if c%2!=m%2 else all(h)
for i in range(200):
    for m in range(6):
        if f(i,17,0,m):
            print(i,m)
            break