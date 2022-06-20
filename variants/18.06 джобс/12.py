k=400*'2'
while '8888' in k or '222' in k:
    if '222' in k:
        k=k.replace('222','88')
    else:k=k.replace('8888','22')
print(k)