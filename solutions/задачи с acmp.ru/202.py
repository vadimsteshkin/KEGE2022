s = input()
t = input()
lst = []
k=len(t)
for i in range(len(s)):
    if s[i:i+len(t)]==t:
        lst.append(i)
print(*lst)
