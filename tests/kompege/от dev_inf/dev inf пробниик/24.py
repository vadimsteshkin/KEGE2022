k=open('24.txt').read()
lst=[]
m=1
for i in range(1,len(k)):
    if k[i]>=k[i-1]:
        m+=1
    else:
        lst.append(m)
        m=1
print(max(lst))