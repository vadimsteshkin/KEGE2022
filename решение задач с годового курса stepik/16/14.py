def F(n,m):
    if m == 0:
        return n
    else:
        return F(m, n % m)
o=0
for 