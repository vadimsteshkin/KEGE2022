k='7'*61
while '777' in k or '73' in k:
    if '777' in k:k=k.replace('777','73',1)
    else:k=k.replace('73','7',1)
print(k)