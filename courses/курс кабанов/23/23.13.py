def f(s,e):
    if s>e or s==43:return 0
    if s==e:return 1
    if s<e: return f(s-1+s,e)+f(s+2,e)+f(s+s+1,e)
print(f(7,63))