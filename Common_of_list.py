n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
g=[]
for i in range(0,len(l)):
    for j in range(0,len(k)):
            if l[i]==k[j]:
                if l[i] not in g:
                    g.append(l[i])
print(*g)
