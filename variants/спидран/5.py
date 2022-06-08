q=0
for i in range(100,999):
    k=str(i)
    s=int(k[1]+k[2])
    k=int(k[0]+k[1])
    s=str(min(s,k)+max(s,k))
    print(s)
    if s=='1216':
        q+=1
        print(s)
print(q)