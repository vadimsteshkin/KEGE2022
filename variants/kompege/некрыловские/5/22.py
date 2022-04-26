for i in range(1,100000):
    x=i
    p=90
    s=6*(x-x%22)
    k=0
    while p<181:
        k+=1
        p+=k
        s=s-2*k
    if s==82:
        print(i)