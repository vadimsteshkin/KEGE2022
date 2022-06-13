a=[]
for _ in range(10000):
    k=bin(_)[2::]
    if _%2:k='1'+k+'0'
    else:k='11'+k+'11'
    if int(k,2)<126:
        print(int(k,2))
        a.append(int(k,2))
print(max(a))