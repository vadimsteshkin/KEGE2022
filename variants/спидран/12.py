m=0
for i in range(101,9999):
    k=i*'1'
    while '111' in k:
        k=k.replace('111','22',1)
        if '222' in k:
            k=k.replace('222','11',1)
    m=max(m,len(k))
    print(m)