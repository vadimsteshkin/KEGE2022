f=open('24_7.txt').readline().replace('ad','a d').replace('da','d a').split()
print(len(max(f,key=lambda x:len(x))))