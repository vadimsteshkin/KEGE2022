k='>'+'1'*28+'2'*18+'3'*35
while '>1' in k or '>2' in k or ">3" in k:
    if '>1' in k:k=k.replace('>1','22>')
    if '>2' in k:k=k.replace('>2','2>1')
    if '>3' in k:k=k.replace('>3','1>2')
k=k.replace('>','')
print(sum([int(i) for i in k]))