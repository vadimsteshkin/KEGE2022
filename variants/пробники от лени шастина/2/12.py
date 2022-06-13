k=81*'1'
while '1111' in k or '88888' in k:
    if '1111' in k:k=k.replace('1111','888',1)
    else:k=k.replace('88888','888',1)
print(k)