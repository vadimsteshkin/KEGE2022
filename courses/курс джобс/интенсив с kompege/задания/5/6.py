for _ in range(9999):
    k=bin(_)[2::]
    if k.count('1')>k.count('0'):k+='1'
    else:k+='0'
    if int(k,2)>36:
        print(int(k,2))