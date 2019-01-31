r,s=map(str,input().split())
k=list(r.split())
c=0
for i in k:
    for j in i:
        if j==s:
            c+=1
print(c)
        
