input()
k=list(map(int,input().split()))
m=0
k.extend(k[0:2])
for i in range(len(k)-2):
    m=max(k[i]+k[i+1]+k[i+2],m)
print(m)