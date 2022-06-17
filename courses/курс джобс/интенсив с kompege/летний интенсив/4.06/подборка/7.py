def f(x,y,a):
    return (x*y>1200) and (x<a) and (y<a)


for a in range(100000):
    if all(f(x,y,a)==0 for x in range(1,1000) for y in range(1,1000)):
        print(a)