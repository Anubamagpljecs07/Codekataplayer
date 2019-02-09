v=['a','e','i','o','u','A','E','I','O','U']
s=input()
g=[]
l=[]
for i in s:
    if i in v:
        g.append(i)
    else:
        l.append(i)
s=""
for i in g:
    s=s+i
for i in l:
    s=s+i
print(s)
