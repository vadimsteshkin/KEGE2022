sk=set()
def f(s,step):
    if step==15:
            sk.add(s)
    else:
        f(s*2,step+1)
        f(s*2+1,step+1)

f(1,0)
print(len(sk))