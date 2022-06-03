k=4**1014+12
for x in range(1,100000):
    k-=2**x
    if bin(k)[2::].count('0')==2000:
        print(x)
