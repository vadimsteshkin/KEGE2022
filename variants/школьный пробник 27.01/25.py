def f(n):
    s =set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s|={i,n//i}
    s1=set()
    for i in s:
        if i%2!=0:
            s1.add(i)
    return s1
for i in range(190061, 190081):
    m=sorted(f(i),reverse=True)
    if len(m)==4:
        print(*m)