def f(x,y,a):
    return ((2*x+y)!=70) or (x<y) or (a<x)
for a in range(100000):
    if all(f(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)