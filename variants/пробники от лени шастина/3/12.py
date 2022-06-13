k='1'*95+31*'7'
while '1111' in k:
    k=k.replace('1111','7',1)
    k=k.replace('77','1')
print(k)