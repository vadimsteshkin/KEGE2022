def f(s, c, m):
    if s >= 41: return c % 2 == m % 2
    if c == m: return 0
    h=[f(s+1,c+1,m),f(s+5,c+1,m),f(s*3,c+1,m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for b in range(40,0,-1):
    for m in range(99):
        if f(b,0, m):
            print(b, m)
            break