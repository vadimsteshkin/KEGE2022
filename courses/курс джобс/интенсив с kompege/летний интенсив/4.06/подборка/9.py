def f(x):
    p= x in {2,4,6,8,10,12,14,16,18,20}
    q=x in {5,10,15,20,25,30,35,40,45,50}
    a=0
    return (a<=p) and (q<=(not(a)))
p=0
for i in range(10000):
    if not(f(i)):
        p+=1
print(p)