n,l1,r=map(int,input().split())
l=list(map(int,input().split()))
g=[]
for i in range(0,len(l)):
    if l[i]==l1:
        a=i
    elif l[i]==r:
        b=i
for i in range(a,b+1):
    g.append(l[i])
m=min(g)
print(m)
