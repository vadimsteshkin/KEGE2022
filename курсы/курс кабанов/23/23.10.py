def f(s,e):
    if s>e or s==6:return 0
    if s==e:return 1
    if s<e: return f(s*3,e)+f(s+2,e)
print(f(1,25)*f(25,63))