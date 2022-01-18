def f(n):
    if n==1:
        return 2
    if n>1 and n%2==0:
        return n+2+f(n-1)
    else:
        return f(2)*f(n-2)
print(f(14))