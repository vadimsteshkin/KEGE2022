def f(x,a):
    return ((x%a) and (x%16!=0))<=(x%23)
for a in range(1,1000):
    if all(f(x,a) for x in range(1,1000)):
        print(a) 
print(not(16%16)<=(16%23))