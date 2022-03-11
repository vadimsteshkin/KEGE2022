a='ABCDEFGH'
k=input()
if (int(k[1])+a.index(k[0].upper()))%2==0:
    print('WHITE')
else:print("BLACK")