for i in range(1,1000):
    k=bin(i)
    for _ in range(2):
        if k.count('1')>k.count('0'):
            k+='0'
        else:
            k+='11'
    if int(k,2)>500:
        print(i)
print(int('130424',5)+1)