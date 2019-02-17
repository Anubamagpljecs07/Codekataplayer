n,k=map(int,input().split())
l=list(map(int,input().split()))
g=[]
for i in l:
    if i>k:
        g.append(i)
print(min(g))
