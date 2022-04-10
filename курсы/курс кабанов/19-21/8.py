k=''
q=1
_=int(input())
while len(k)<=_:
    k+= q*(str(q)+'')
    q+=1
print(' '.join(k[:_]))

