n=int(input())
l=list(map(int,input().split()))
g=[]
for i in range(0,len(l)-1):
    m=max(l[i],l[i+1])
    g.append(m)
print(*g)
