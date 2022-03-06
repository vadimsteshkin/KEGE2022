q=ma=0
for m in range(1,100,2):
    for n in range(0,101,2):
        if 100_000_000<=2**m*7**n<=300_000_000:
            q+=1
            ma=max(ma,m+n)
print(q,ma)