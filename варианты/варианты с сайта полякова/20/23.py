def f(s,e):
    if int(s)<int(e):return 0
    if s==e:return 1
    else: return f(int(s,2)-1,e)+f(s-'1',e)
print(f)