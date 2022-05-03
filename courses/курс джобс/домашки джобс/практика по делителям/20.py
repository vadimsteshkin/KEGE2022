q,ma=0,0
for c in range(5000):
    for a in range(5000):
        for b in range(5000):
            if c**2==a**2+b**2:
                q+=1
                ma=max(ma,a+b+c)
print(q,ma)