s=input()
s=list(s.split(" "))
g=[]
for i in range(0,len(s)):
    if i==0 or i==len(s)-1:
        g.append(s[i])
    else:
        g.append(s[i][::-1])
print(*g)
