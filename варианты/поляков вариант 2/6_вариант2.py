i=0
for s in range(10000):
    n = 1
    while s > n:
        s = s - 15
        n = n * 5
    if n==125:
        i+=1
    print(i)
#115