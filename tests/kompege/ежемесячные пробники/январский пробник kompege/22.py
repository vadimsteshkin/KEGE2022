for i in range(1,1000000):
    x=i
    a=0
    b=0
    while x>0:
        if x%2==0:
            a+=1
        else: b+=x%6
        x//=6
    if a==1 and b==4:
        print(i)