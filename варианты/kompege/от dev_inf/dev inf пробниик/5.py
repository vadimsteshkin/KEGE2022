for i in range(6,100000):
    x=bin(i)[2::]
    for _ in range(2):
        p=sum([int(a) for a in x])
        if p%2==0:
            x+='0'
        else:x+='1'
    if int(x,2)>60:
        print(int(x,2))