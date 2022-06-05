k='>'+15*'1'+20*'2'+25*'3'
while '>1' in k or '>2' in k or '>3' in k:
    if '>1' in k:k=k.replace('>1','22>',1)
    if '>2' in k: k = k.replace('>2', '2>1',1)
    if '>3' in k: k = k.replace('>3', '1>',1)
print(sum([int(i) for i in k if i!='>']))