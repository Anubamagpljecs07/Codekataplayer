n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k-1):
	m=min(l)
	l.remove(m)
n=min(l)
print(n)
