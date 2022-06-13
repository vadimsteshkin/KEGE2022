k='1'*50+'2'*50+'3'*50
while '23' in k or '21' in k or '31' in k:
    if '21' in k:k=k.replace('21','12')
    if '31' in k:
        k=k.replace('31','13')
    if '23' in k:k=k.replace('23','32')
print(k[29],k[89],k[129])