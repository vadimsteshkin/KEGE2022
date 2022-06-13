for i in range(10):
    for j in range(10):
        k=int(f'12345{i}6{j}8')
        if k%17==0:
            print(k,k//17)