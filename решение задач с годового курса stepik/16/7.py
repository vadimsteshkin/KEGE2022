from functools import *


@lru_cache()
def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return f(n - 1) + 2 * f(n / 2)
    else:
        return f(n - 1) + f(n - 3)


o = 0
for i in range(1, 1000):
    m = f(i)
    if m < 10 ** 8:
        o += 1
print(o)
