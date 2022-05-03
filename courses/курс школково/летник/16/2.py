def f(n):
    if n==1: return 1
    if n==2 or n==3: return 1
    if n>3 and n%2==0: return f(n-1) +f(n-3)+f(n//3)
    else: return f(n-2)+f(n-1)
print(f(30))