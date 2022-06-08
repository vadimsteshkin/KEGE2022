f=[i for i in open('24.txt')]
k=max(f,key=lambda x:x.count('B'))
print(f.index(k)+1,max([i for i in k], key=lambda x:k.count(x)))