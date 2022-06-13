def f(x,y,a):
    print(a,(a<x) or (y<=x))
    return  (a<x) or (y<=x)
for a in range(100000):
    if all((f(x,y,a)==0) for x in range(1,8) for y in range(7,10000)):
        print(a)
        break