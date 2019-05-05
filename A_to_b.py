#G
n,l1,r=map(int,input().split())
l=list(map(int,input().split()))
g=[]
for i in range(l1-1,r):
    g.append(l[i])
m=min(g)
print(m)
    
