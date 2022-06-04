k='>'+25*'1'+17*'2'+10*'3'
while '>1' in k or '>2' in k or '>3' in k:
    if '>1' in k:k=k.replace('>1','22>3')
    if '>2' in k:k=k.replace('>2','2>')
    if '>3' in k:k=k.replace('>3','11>2')
print(sum([int(i) for i in k[0:-1]]))