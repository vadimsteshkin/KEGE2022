def f(s,e):
    if s>e or s==12:return 0
    if s==e:return 1
    else:return f(s+1,e)+f(s+4,e)+f(s*2,e)
print(f(7,22))