k='>'+'1'*11+12*'2'+30*'3'
while '>1' in k or '>2' in k or ">3" in k:
    if '>1' in k:
        k=k.replace('>1','22>',1)
    if '>2' in k:
        k=k.replace('>2',"222>",1)
    if '>3' in k:
        k=k.replace('>3','1>',1)
k=k[:len(k)-1]
print(sum([int(x) for x in k]))