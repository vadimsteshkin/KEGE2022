def f(s,e):
    if s>e or s==15:return 0
    if s==e:return 1
    else:return f(s+1,e)+f(s*2,e)
print(f(2,12)*f(12,32))
