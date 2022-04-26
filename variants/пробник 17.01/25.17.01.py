def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return sorted(s)
for i in range(550_000,9999999999):
    o=[x for x in d(i) if x%10==7]
    if len(o)==3:
        print(i,o[-1])
