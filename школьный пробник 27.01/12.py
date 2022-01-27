f='5'*69
while '333' in f or '555' in f:
    if '555' in f:
        f=f.replace('555','3',1)
    else:f=f.replace('333','5',1)
print(f)
