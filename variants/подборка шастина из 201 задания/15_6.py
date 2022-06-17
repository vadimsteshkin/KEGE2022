def f(x,y,a):
    return ((2*x+3*y)!=135) or (a<y) or (a<x)
for a in range(100000):
    if all(f(x,y,a) for x in range(1,1000) for y in range(1,1000)):
        print(a)