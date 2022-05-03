k=107*'X'
while 'XXX' in k or'ZYX' in k or 'ZXX' in k:
    k=k.replace('XXX','ZZ',1)
    k=k.replace('ZYX','X',1)
    k=k.replace('ZXX','Y',1)
print(k)