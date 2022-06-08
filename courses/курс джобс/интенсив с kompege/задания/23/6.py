def f(s,e):
    if s<e:return 0
    if s==e:return 1
    else:return f(s-8,e)+f(s//2,e)
print(f(102,43)*f(43,5))