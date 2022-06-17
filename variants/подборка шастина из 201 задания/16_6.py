def f(n):
    if n==1:
        return 1
    if n%2==0:
        return 4*f(n/2)
    return f(n-2)+3*n
print(f(42))