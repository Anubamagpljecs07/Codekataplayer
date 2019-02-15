def isprime(n):
	c=0
	for i in range(2,n):
		if n%i==0:
			c+=1
	if c==0:
		a=1
	else:
		a=0
	return a
s=input()
g=[]
for i in s:
	if i!=" ":
		g.append(i)
f=len(g)
s=isprime(f)
if s==1:
	print("yes")
else:
	print("no")
