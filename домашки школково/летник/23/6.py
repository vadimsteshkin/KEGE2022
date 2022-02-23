def f(s,e):
    if s>e:return 0
    if s==e:return 1
    else:return f(s+2,e)+f(s+3,e)+f(s*2,e)
print(f(3,8)*f(8,18))