def F(n):
    if n < 10:
        return n
    else:
        m = F(n // 10)
        d = m % 10;
        if m < d:
            return d
        else:
            return m


for i in range(100, 1000):
    if F(i) > 7:
        print(i)
