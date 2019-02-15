s=input()
g=[]
l=['a','b']
for i in s:
    if i not in g:
        g.append(i)
if g==l:
    print("yes")
elif len(g)==1:
    if l[0]=='a' or l[0]=="b":
        print("yes")
else:
    print("no")
