def f(n):
    if n==1: return 0
    if n==2 or n==3: return 1
    else: return f(n-1)+n**2+f(n-2)
print(f(19))