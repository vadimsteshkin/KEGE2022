
def f(n):
    if n<0:
        return -n
    if n%2:
        return 4*n+2*f(n-4)
    else:return 2*n+1+f(n-3)
print(f(33))