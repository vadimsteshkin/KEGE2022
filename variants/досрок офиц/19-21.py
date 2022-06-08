def f(a, b, c, m):
    if a + b >= 231: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for a in range(213, 1, -1):
    for m in range(1, 5):
        if f(17, a, 0, m)
            print(a, m)
            break
