k=list(map(int,input().split()))
pr=k[1]
s=k[0]
f=True
for x in range(1,s):
        for y in range(1,pr//x+1):
            if f==True:
                if x+y==s and x*y==pr:
                    l=min(x,y)
                    o=max(x,y)
                    print(l,o)
                    f=False
                    break
