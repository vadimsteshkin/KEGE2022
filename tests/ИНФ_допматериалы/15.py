def f(x,a):
    return ((x%3==0)<=(x%5!=0)) or ((x+a>=90))
for a in range(100000):
    if all(f(x,a) for x in range(1000)):
        print(a)
        break