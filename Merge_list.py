n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in k:
	l.append(i)
g=sorted(l)
print(*g)
