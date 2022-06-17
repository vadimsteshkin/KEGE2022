def f(x,a):
    return (x%a!=0)<=((x%6==0) <=(not(x%9)))
for a in range(1,10000):
    if all(f(x,a) for x in range(1,100000)):
        print(a)