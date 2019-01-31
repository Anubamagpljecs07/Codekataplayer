p,a=map(int,input().split())
c=0
for i in range(1,a):
	for j in range(1,a):
		if 2*(i+j)==p and i*j==a:
			c+=1
			if c==1:
				print("yes")
				break
		if c==1:
			break
if c==0:	
	print("no")
