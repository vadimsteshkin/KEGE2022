for i in range(8,9999):
    m=i
    m-=m%8
    m=bin(m)[2::]
    k=sum([int(j) for j in m.split()])
    if k%2==0:
        m+='00'
    else:
        m+='01'
    if int(m,2) >353:
        print(i)