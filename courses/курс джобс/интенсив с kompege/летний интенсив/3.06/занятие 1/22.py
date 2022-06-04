k=147*'3'
while '5555' in k or '3333' in k:
    if '5555' in k:
        k=k.replace('5555','3',1)
    else:k=k.replace('3333','5',1)
print(k)