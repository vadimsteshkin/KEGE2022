for _  in range(100):
    k=bin(_)[2::]
    for i in range(3):
        if k.count('0')==k.count('1'):k+=k[-1]
        else:k+=sorted(k,key=lambda x:k.count(x))[0]
    k=int(k,2)
    if k%4==0 and k%8!=0:
        print(_)