lst=[int(x) for x in open('27-B_4.txt')][1::]
o=0
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if (lst[j] +lst[i])%10==0:
            o+=1
print(o)
# 15 5001021