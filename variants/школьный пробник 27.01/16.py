def f(n):
    if n==1:return 1
    if n>1:return 3*f(n-1)+g(n-1)-n+5

def g(n):
    if n==1:return 1
    if n>1:return f(n-1)+3*g(n-1)-3*n

print(g(14)+f(14))
