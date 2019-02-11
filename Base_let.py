r,s=map(str,input().split())
g=[]
h=[]
for i in r:
    if i not in g:
        g.append(i)
for i in s:
    if i not in h:
        h.append(i)
c=0
for i in g:
    if g.count(i)==h.count(i):
        c+=1
if c==len(g) and c==len(h):
    print("true")
else:
    print("false")
