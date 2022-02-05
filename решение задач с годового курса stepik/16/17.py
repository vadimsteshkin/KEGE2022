def F(n):
    if n > 0:
        d = (n % 10 + F(n // 10))
        return d
    else:return 0
for i in range(1,1000000):
    if F(i)>51:
        print(i)


