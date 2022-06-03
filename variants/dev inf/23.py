def f(s,e,c):
    if c>6 or s>e:return 0
    if s==e and c==6:return 1
    else:return f(s+1,e,c+(not(s%2)))+f(s+3,e,c+(not(s%2)))+f(s+5,e,c+(not(s%2)))
print(f(2,25,0))
