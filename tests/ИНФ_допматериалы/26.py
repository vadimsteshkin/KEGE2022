f=sorted([list(map(int, i.split())) for i in open('107_26.txt')][1::],reverse=True)
m,k=1,0
for i in f:
    if i[0]==m and (k-i[1])==14:
        print(m,i[1]+1)
        break
    k=i[1]
    m=i[0]

