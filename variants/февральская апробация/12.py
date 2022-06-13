k='2'*52
while '222' in k or '000' in k:
    if '000' in k:
        k=k.replace('000','2',1)
    else:k=k.replace('222','02',1)
print(k)