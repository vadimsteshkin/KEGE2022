def f(s,e):
    if s>e or s==11 or s==18:return 0
    if s==e:return 1
    if s<e: return f(s*3,e)+f(s+2,e)+f(s+1,e)
print(f(4,8)*f(8,23))