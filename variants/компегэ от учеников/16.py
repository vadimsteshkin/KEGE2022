def f(n,r):
    if n==0:return 2*r
    else:return f(n//10, r*10+n%10)
for n in range(100000000):
    k=f(n,0)
    if k==628648:
        print(n)