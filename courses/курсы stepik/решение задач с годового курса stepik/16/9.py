def f(n):
    if n <= 13: return n ** 3 + n ** 2 + 1
    if n > 13 and n % 3 == 0:
        return f(n - 1) + 2 * n ** 2 - 3
    else:
        return f(n - 2) + 3 * n + 6


o = 0
for i in range(1, 1001):
    k = str(f(i))
    m = [int(x) for x in k if int(x) % 2 == 0]
    if len(m) == 0:
        o += 1

print(o)
