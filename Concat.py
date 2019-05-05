#G
s,m=map(str,input().split())
a=len(s)
b=len(m)
g=""
if a>b:
	g=g+s[:b]+m
elif b>a:
	g=g+m[:a]+s
else:
	g=g+s+m
print(g)
