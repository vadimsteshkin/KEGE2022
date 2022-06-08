def f(x,y, a):
    return (2*x+3*y==101) and (y+x<a)
for a in range(1,10000):
    if all(f(x,y,a)==0 for x in range(1000) for y in range(1000)):
        print(a)