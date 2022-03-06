k=500*'5'
q=0
while '555' in k or '333' in k:
    if '333' in k:
        k=k.replace('333','5',1)
        q+=3
    else:
        k=k.replace('555','3',1)
print(q)