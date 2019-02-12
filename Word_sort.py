s=input()
s=list(s.split(" "))
g=[]
a=[]
for i in s:
	i=list(i)
	g.append(sorted(i))
	g.append(' ')
for i in g:
	for j in i:
			a.append(j)
f=""
for i in a:
	f=f+i
print(f)
