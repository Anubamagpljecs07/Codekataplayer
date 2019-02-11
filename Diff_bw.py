s=input()
r=input()
g=[]
if " " in s and " " in r:
    s=list(s.split(" "))
    r=list(r.split(" "))
    if len(r)>len(s):
        for i in r:
            if i not in s:
                g.append(i)
    elif len(s)>len(r):
        for i in s:
            if i not in r:
                g.append(i)
    print(*g)
else:
    if len(s)>len(r):
        for i in s:
            if i not in r:
                g.append(i)
    elif len(r)>len(s):
        for i in r:
            if i not in s:
                g.append(i)
    print(*g)
