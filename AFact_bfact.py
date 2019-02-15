def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
n,m=map(int,input().split())
a=min(m,n)
g=fact(a)
print(g)
