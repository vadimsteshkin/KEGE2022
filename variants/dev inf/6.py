for i in range(5,50):
    k=0
    s=i
    n=s
    s//=10
    while s+n<125 or k<5:
        s+=n
        n-=5
        k+=1
        print(s,n,i)
    if n>10:
        print(i,n)