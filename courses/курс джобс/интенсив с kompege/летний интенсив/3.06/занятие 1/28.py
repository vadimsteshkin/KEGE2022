def f(x,a):
    return x%25==0 and (x%24==0 and x%75==0<=x%a==0)
for a in range(1,10000):
    if all(f(x,a) for x in range(100)):
        print(a)