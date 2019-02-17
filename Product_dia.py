n=int(input())
l=[]
g=[]
s,f=0,0
a=1
for i in range(0,n):
    l.append(input().split())
for i in range(0,n):
    s=s+int(l[i][i])
g.append(s)
for i in range(0,n):
    x=n-i-1
    f=f+int(l[i][x])
g.append(f)
for i in g:
    a=a*int(i)
print(a)
    
