s=set()
for i in range(3,30):
    k=i*'8'
    while '555' in k or '888' in k:
        k=k.replace('555','88',1)
        k=k.replace('888','55',1)
    s.add(k)
    print(len(s))