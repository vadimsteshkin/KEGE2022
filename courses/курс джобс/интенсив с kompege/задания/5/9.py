for _ in range(81,9999):
    k=bin(_)[2::]
    for i in range(3):
        if k.count('1')==k.count('0'):k+=k[-1]
        else:
            if k.count('1')>k.count('0'):k+='0'
            else:k+='1'
    if int(k,2)%4!=0 and int(k,2)%2==0:
        print(_)
        break