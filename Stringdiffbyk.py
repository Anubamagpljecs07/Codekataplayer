r,s,k=map(str,input().split())
c=0
for i in range(0,len(r)):
    for j in range(0,len(s)):
        if i==j:
            if r[i]!=s[j]:
                c+=1
if c==int(k):
    print("yes")
else:
    print("no")
