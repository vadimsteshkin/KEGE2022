k=open('24_15.txt').read()
for i in range(1,100):
    if k.count(i*'D') >0:
        print(i)

