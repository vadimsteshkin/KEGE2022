def f(x,a):
    return not(x%a) or (not(x%2205)) or (x%2800)
for a in range(1,1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a)
        break