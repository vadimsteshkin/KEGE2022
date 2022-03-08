n=int(input())
lst=[]
for i in range(2,int(pow(n,0.5))+1):
    if n %i==0:
      print(i)
      n=n // i
      if n>1: print('*')
    else: i+=1
