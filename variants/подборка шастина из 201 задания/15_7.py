def f(x,a):
    return ((x%3==0)<=(x%5!=0)) or (x+a>=70)
for a in range(1,10000):
    if all(f(x,a) for x in range(1,100000)):
        print(a)