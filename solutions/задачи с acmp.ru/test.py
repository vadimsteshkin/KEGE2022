for i in range(100,1000):
    if i%100!=0:
        print(i,i/sum([int(k) for k in str(i)]))