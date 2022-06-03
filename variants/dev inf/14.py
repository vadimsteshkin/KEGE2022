q=0
for i in range(3,96):
    k=i
    s=''
    while k>0:
        s+=str(k%3)
        k//=3
    if s[0]+s[1]=='12':
        k=i
        s = ''
        while k > 0:
            s += str(k % 5)
            k//=5
        if s[-1]=='3':
            q+=i
print(q)