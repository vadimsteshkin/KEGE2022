for _ in range(1,10000):
    x=_
    s=''
    while x>0:
       s+=str(x%9)
       x//=9
    s=s[::-1]
    for i in range(5):
        if s.count('7')==s.count('5'):
            s+=s[-1]
        else:s+=max(sorted(s)[::-1],key=lambda x:s.count(x))
    om=hex(int(s,9))[2::]
    if 'bac' in om:
        print(_)