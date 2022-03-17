def f(x,y,a):
    return (5*x+6*y<121) or (y>a) or (x>a)
for a in range(1000):
    if all(f(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)