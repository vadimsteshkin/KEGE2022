def f(n,m):
    if m<=5 and n<=2:
        return 2
    if n>2 and m>5:
        return f(n-3,m)+f(n,m-2)*m +f(n-5,m-5)*n
print(f(11,16))