# k=[int(i) for i in open('27-76a.txt')]
# m=0
# for i in range(1,k[0]):
#     for j in range(i+2,k[0]+1):
#         if (k[i]+k[j]) %3==0 and sum(k[i+1:j])%2==0:
#             m+=1
# print(m)