def F(n):
    print(n)
    if n > 0:
        d = (n % 10 + F(n // 10))
        print(d)
        return d
    else:
        return 0
f=F(10)
print(f)
