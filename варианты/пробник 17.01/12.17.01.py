o=0
for i in range(3,101):
    m=i*'1'
    while '111' in m or '88888' in m:
        if '111' in m:
            m=m.replace('111','88',1)
        else:
            m=m.replace('88888','8',1)
    if len(m)>o:
        print(i)
        o=len(m)
