def f(n):
    if n<=1:
        return 1
    if n%2==0 and n>1:return f(n-1)*n
    else:return n+f(n-2)
print(f(84))