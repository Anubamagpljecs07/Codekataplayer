def vow(x):
	c=0
	v=['a','e','i','o','u']
	for i in x:
		if i in v:
			c+=1
	if c>=1:
		a=1
	else:
		a=0
	return a
n=int(input())
g=[]
d=0
for i in range(0,n):
	g.append(input())
for i in g:
	if vow(i)==1:
		d+=1
if d==len(g):
	print("yes")
else:
	print("no")
