k=70*'8'
while '2222' in k or '8888' in k:
    if '2222' in k:k=k.replace('2222','88',1)
    else:k=k.replace('8888','22',1)
print(k)