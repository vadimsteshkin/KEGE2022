def pr(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
q=0
w=0
for i in range(9999971,10_000_000,1):
    if pr(i):
        print(abs(10_000_000-i),i)
        w+=1
    if w==3:
        break
for j in range(10_000_000,99999999999999):
    if pr(j):
        print(abs(10_000_000-j),j)
        q+=1
    if q==3:
        break