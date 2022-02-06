k='1'*46+'2'*31
while '1111' in k:
    k=k.replace('1111','2',1)
    k=k.replace('222','1',1)
print(k)