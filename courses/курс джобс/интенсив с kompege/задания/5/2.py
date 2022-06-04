for _ in range(222):
    k=bin(_)[2::]
    if _%2:k+='0'
    else:k='1'+k
    if sum([int(i) for i in k])%2:k+='0'
    else:k+='1'
    if int(k,2)>228:
        print(_)
        break