def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    if len([i for i in s if i%2])==5:
        return True
    return False
for i in range(88535,153374):
    if d(i):
        print(i)