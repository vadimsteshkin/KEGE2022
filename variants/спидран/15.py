def f(x,y,a):return ((x*y)<a) or (x<y) or (x>=12)
for a in range(1000):
    if all(f(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)
        break