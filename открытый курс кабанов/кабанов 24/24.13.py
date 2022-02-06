k=open('24_13.txt').readline()
c=m=k[0]
for i in range(1,len(k)):
    if k[i-1]>k[i]:
        c+=k[i]
        m=max(m,c,key=len)
    else:
        c=k[i]
print(m)