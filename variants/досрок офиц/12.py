k=84*'8'
while '1111' in k or '8888' in k:
    if '1111' in k:
        k=k.replace('1111','8',1)
    else:k=k.replace('8888','11',1)
print(k)