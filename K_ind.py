n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,len(l)):
	if l[i]==k:
		print(i+1)
