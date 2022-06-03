def f(n):
    if n<5:
        return 5-n
    if n>=5 and n%3==0:
        return 4*(n-5)*f(n-5)
    else:
        return 2*f(n-1)+f(n-2)+3*n
print(f(20))