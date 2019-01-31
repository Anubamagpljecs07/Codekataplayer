n=int(input())
l=list(map(int,input().split()))
g=[]
for i in l:
    c=l.count(i)
    g.append(c)
m=max(g)
print(m)
