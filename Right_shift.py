n,k=map(int,input().split())
g=list(map(int,input().split()))
for i in range(0,k):
    g.insert(0,g[-1])
    del(g[-1])
print(*g)
