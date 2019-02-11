s=int(input())
c=0
for i in range(1,s+1):
	for j in range(1,s+1):
		if (i*3)==s:
			c+=1
		elif (i*7)==s:
			c+=1
		elif (i*3)+(j*7)==s:
			c+=1
if c>=1:
	print("yes")
else:
	print("no")
	
