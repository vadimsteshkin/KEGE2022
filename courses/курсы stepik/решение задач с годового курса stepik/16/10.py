def f(n):
    if n > 25:
        return n ** 2 + 2 * n + 1
    else:
        if n % 2 == 0:
            return 2 * f(n + 1) + f(n + 3)
        else:
            return f(n + 2) + 3 * f(n + 5)


o = 0
for i in range(1, 1001):
    m = [x for x in str(f(i)) if x == '0']
    if len(m) == 0:
        o += 1
print(o)
