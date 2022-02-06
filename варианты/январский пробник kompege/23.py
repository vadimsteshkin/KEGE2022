def f(s,e):
    if s>e:return 0
    if s==e or s==10 or s==15:return 1
    else:return f(s+1,e)+f(s+2,e)+f(s+3,e)
print(f(5,11)*f(11,18))