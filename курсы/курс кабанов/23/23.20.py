sk=set()
def f(s,step):
    if step==8:
        if 1000<=s<=1024:
            sk.add(s)
    else:
        f(s+1,step+1)
        f(s+5,step+1)
        f(s*3,step+1)
f(1,0)
print(sk)