for i in range(11,12000):
    k=i
    s=''
    while k>0:
        s+=str(k%3)
        k//=3
    s=s[::-1]
    s+=str(i%3)
    u=int(s,3)
    if u>99:
        print(u)
        break