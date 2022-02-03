for i in range(1,88):
    x=bin(i)[2::]
    for _ in range(2):
        if x.count('1')%2==0:
            x+='0'
        else:x+='1'
    if int(x,2)>103:
        print(i)