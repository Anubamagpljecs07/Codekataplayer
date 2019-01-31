r,s=map(str,input().split())
k=list(r.split())
c=0
for i in k:
    for j in i:
        c+=1
        if j==s:
            print(c)

