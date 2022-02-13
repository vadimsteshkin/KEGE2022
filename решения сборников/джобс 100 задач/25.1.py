def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return len(s)
for i in range(10002000,10200001):
    if d(i)>349:
        print(i, sum([int(x) for x in str(i)])) 