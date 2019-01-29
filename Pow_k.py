n,k=map(int,input().split())
c=0
for i in range(0,n):
	if pow(k,i)==n:
		print("yes")
		c+=1
		break
if c==0:
	print("no")
