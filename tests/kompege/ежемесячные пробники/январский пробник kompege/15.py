def f(x,a):
    return (x&30!=4) or ((x&35==1)<=(x&a==0))
for a in range(1,100000):
    if all((f(x,a)==1) for x in range(1,100000)):
        print(a)