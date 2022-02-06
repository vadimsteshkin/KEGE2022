def f(n):
    if n <= 1:
        return 0
    if n > 1 and n % 2 == 1:
        return 3 * n ** 2 + f(n - 1)
    else:
        return n / 2 + f(n - 1) + 2


print(int(f(49)))
