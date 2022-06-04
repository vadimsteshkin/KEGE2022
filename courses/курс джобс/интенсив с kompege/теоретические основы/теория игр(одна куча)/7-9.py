def f(s, p, c, m):
    if s >= 43: return c % 2 == m % 2
    if c == m: return 0
    if p != '3': h = [f(s + 2, '2', c + 1, m), f(s + 1, '1', c + 1, m)]
    if p != '1': h = [f(s * 2, '3', c + 1, m), f(s + 2, '2', c + 1, m)]
    if p != '2': h = [f(s * 2, '3', c + 1, m), f(s + 1, '1', c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for b in range(42,1,-1):
    for m in range(99):
        if f(b, '', 0, m):
            print(b, m)
            break
