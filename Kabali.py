s="kabali"
m=int(input())
l=[]
d=0
for var in range(0,m):
    l.append(input())
for j in l:
    c=0
    for i in j:
        if i in s:
            if j.count(i)==s.count(i):
                c+=1
    if c==len(j):
        d+=1
print(d)
