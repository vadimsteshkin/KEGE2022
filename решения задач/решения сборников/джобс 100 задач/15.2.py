def f(x,y,a):
    return ((3*x+4*y)!=101) or (x<a) or (3*y<=a)
for a in range(1,1000):
    if all(f(x,y,a) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break