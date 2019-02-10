n=int(input())
l=list(map(int,input().split()))
g=[]
for i in l:
    if i<0:
        g.append(i)
s=0
for i in g:
    s=s+i
print(s)
