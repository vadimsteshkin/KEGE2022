for _ in range(10000):
    k=bin(_)[2::]
    if _%2:k+='0'
    else:k='1'+k
    if k.count('1')%2==0:k+='1'
    else:k+='0'
    if int(k,2)>228:print(_)