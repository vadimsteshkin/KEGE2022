def f(x, a):
    return (x & 57 != 0) and (x & 38 != 0) or (x & 9 == 0) or (x & a == 0)


for a in range(1,10000):
    if all(f(x, a)==1 for x in range(10000)):
        print(a)
        break
