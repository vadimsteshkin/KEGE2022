def f(n):
    if n<=1:
        return 0
    else:
        if n%2==0:
            return n//2+f(n-1)+2
        else:return 3*n**2+f(n-1)
print(f(49))