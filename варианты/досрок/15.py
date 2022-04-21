def f(x,a):
    return ((x%3)<=(not(x%5))) or ((x+a)>=70)
for a in range(1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a)