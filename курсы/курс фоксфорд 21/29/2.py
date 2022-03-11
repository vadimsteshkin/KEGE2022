def f(x,y,a):
    return ((y+2*x)<a) or((y+x)>6) or ((y-x)<4)
for a in range(1,10000):
    if all(f(x,y,a) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break