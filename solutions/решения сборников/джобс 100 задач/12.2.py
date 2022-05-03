for i in range(1,88):
    for j in range(1,80):
        k='0'+i*'1'+j*'2'
        while '02' in k or '01' in k:
            if '01' in k:
                k=k.replace('01','20',1)
            else:
                k=k.replace('02','2101',1)
    s=sum([int(x) for x in k])
    if s==123:
        print(i)
        break