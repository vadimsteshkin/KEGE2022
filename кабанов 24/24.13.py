k=list(open('24_13.txt').readline())
print(k)
lst=set()
lt=[]
for i in range(len(k)-1):
    if k[i]>k[i+1]:
        lst|={k[i],k[i+1]}
    else:
        lst=list(lst)
        lt.extend([lst])
        lst=set()
print(lt)