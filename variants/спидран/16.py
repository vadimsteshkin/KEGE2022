def f(n):
    if n==1:
        return 1
    else: return f(n-1)*(n+1)
print(f(4))