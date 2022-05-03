def F(n):
    global o
    o += 1
    if n >= 1:
        o += 1
        F(n - 1)
        F(n // 2)


o = 0
F(140)
print(o)
