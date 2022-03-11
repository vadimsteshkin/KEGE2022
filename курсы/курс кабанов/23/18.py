def f(s,e,step):
    if s>e:return 0
    if s==e and step!=7: return 0
    if s==e and step ==7:
        return 1
    else:
        return f(s+1,e,step+1)+f(s+4,e,step+1)+f(s*2,e,step+1)
print(f(3,27,0))