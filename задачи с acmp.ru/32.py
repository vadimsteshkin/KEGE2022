a=sorted(input(),reverse=True)
if int(a)<0:

b=input()
if int(b)>0:
    b1=sorted(b)
    i=0
    f=True
    while f or i!=len(b1):
        if b1[i]!='0':
            f=False
        i+=1
    s=b1[i-1]
    b1.remove(s)
    b1.insert(0,s)
    print(int(''.join(a))-int(''.join(b1)))
elif int(b)==0:
    print(int(''.join(a))-int(b))
elif int(b)<0: 
    b1=sorted(b,reverse=True)
    b1.remove('-')
    print(int(''.join(a))+int(''.join(b1)))
