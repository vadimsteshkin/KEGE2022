def f(n):
    if n<=2:
        return n
    else:
        return f(n-2)+g(n)
def g(n):
    if n<=2:
        return n
    else:
        return f(n-1)-g(n-2)
print(g(15))