n=int(input())
l=list(map(int,input().split()))
g=[]
for i in l:
    if i<n:
        g.append(i)
h=sorted(g)
print(*h)
