f=open('24.txt').readline()
f=f.replace('AB','*').replace('CB','*').replace('B',' ').replace('A',' ').replace('C',' ').split()
print(len(max(f,key=lambda  x:len(x))))