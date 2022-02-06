def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2)
    else:
        return 1 + f(n - 1)


for i in range(1, 10000):
    if f(i) == 12:
        print(i)
        break
