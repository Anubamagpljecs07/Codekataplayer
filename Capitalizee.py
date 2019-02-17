s=input()
g=""
for i in s:
    if i==" " or s.count(i)==1:
        g=g+i
    else:
        g=g+i.upper()
print(g)
