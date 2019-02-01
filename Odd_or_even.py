n=int(input())
c=0
l=list(map(int,input().split()))
for i in l:
	if i%2==0:
		c+=1
if c>=2:
	for i in l:
		if i%2==1:
			print(i)
else:
	for i in l:
		if i%2==0:
			print(i)
