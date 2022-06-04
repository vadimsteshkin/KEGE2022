s=[]
q=0
for _ in range(1,257):
    k=bin(_)[2::]
    if _ %2:
        k='1'+k+'00'
    else:
        k='11'+k+'0'
    q+=s.count([int(k,2)])
    s.append([int(k,2)])
print(q)