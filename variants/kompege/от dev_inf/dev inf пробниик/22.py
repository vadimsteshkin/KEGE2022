for i in range(1,1000):
    x=i
    a=0
    b=1
    while x>0:
        a+=1
        b*=(x%10)
        x//=10
        if a==2 and b==15:
            print(i)