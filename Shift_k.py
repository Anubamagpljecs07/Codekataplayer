n,k=map(str,input().split())
g=list(n)
for i in range(0,int(k)):
    g.insert(0,g[-1])
    del(g[-1])
print("".join(g))
