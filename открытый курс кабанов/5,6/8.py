for _ in range(1,1004):
    s=bin(_)[2::]
    if _%2==0:
        s+='0'
        s='1'+s
    else:
        s+='11'
        s='11'+s
    if int(s,2)>52:
        print(int(s,2))
        break