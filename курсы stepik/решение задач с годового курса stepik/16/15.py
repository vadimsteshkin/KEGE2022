def F(n, m):
    if m == 0:
        d = 1
    else:
        d = n * F(n, m - 1)
    return d
o=0
for x in range(1,1000):
    if F(x,2) in range(100,1001):
        o+=1
print(o)