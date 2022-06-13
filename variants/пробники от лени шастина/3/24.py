f=open('24.txt').readline().split('.')
print(len(max([i for i in f if i.count('A')>2],key=lambda x:len(x))))