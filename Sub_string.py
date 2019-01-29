r,s=map(str,input().split())
c=0
if len(s)>len(r):
	print("no")
else:
	if s in r:
		print("yes")
	else:
		print("no")
