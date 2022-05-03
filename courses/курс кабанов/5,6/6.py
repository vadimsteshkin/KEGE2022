for i in range(1,100):
    k=bin(i)[2::]
    k=k[::-1]
    if int(k,2)==13:
        print(i)
