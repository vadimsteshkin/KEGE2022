def p(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={n//i,i}
    u=set()   
    u.add(0)    
    for k in s:
        if str(k)==str(k)[::-1] and k>10:
            u.add(k)
    return max(u)
for i in range(12345,12426):
    m=p(i)
    if m!=0:
        print(i,m)