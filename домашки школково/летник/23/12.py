def f(s,e):
    if s>e or s==14:return 0
    if s==e:return 1
    else:return f(s+1,e)+f(s+5,e)
print(f(3,21))