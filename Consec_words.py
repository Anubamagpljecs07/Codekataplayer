n=int(input())
g=[]
c=0
for i in range(n):
    g.append(input())
for i in range(0,len(g)):
    if i<len(g)-1 and g[i]==g[i+1]:
        c+=1
    elif i==len(g)-1 and g[i]==g[i-1]:
        c+=1
if c>=1:
    print("yes")
else:
    print("no")
