def f(n):
    if n == 0:
        return 2
    if 0 < n <= 15: return f(n - 1)
    if 15 < n < 95: return 1.6 * f(n - 3)
    if n >= 95: return 3.3 * f(n - 2)


k = int(f(33))
m = 0
for i in str(k):
    print(i, str(k).count(i))
    m = max(m, str(k).count(i))
print(m)
