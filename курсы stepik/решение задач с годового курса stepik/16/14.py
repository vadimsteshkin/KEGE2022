def F(n,m):
    if m == 0:
        return n
    else:
        return F(m, n % m)
o=0
for x in range(100,1001):
    for y in range(100,1001):
        if F(x,y)==30:
            o+=1
            x+=1
print(o)