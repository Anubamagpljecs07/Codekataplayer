n=int(input())
c,d=0,0
l=list(map(int,input().split()))
for i in range(0,len(l)):
	if l[i]==max(l):
		c+=1
		if c==1:
			a=i
	elif l[i]==min(l):
		d+=1
		if d==1:
			b=i
g=abs(a-b)
print(g)
