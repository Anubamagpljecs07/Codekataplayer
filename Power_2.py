n=int(input())
for i in range(0,n+1):
	if pow(2,i)==n:
		print("yes")
		break
else:
	print("no")
