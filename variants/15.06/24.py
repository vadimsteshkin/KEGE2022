f=open('24.txt').readline()
q=0
m=0
while 'CACAC' in f:
    f=f.replace('CACAC','CAC CAC')
print(len(max(f.replace('AB','**').replace('CAC','***').replace('A',' ').replace('C',' ').replace('B',' ').split(),key=len)))