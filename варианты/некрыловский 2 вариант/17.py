f=[int(x) for x in open('17.txt')]
lst=[]
for i in range(len(f)-1):
    m=f[i]+f[i+1]
    s=f[i]*f[i+1]
    if m%3==0 and m%6!=0 and s%10==8:
        lst.append(m)
print(len(lst),sorted(lst)[-1])


