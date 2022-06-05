k='23'*15+'0'*30
while '23' in k:
    if '230' in k:
        k=k.replace('230','2',1)
    else:k=k.replace('23','3',1)
print(sum([int(i) for i in k]))