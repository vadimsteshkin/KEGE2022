q=0
k=6*512**180+7*64**181+3*8**184+5*8**125-65
while k>0:
    if k%64==0:
        q+=1
    k//=64
print(q)