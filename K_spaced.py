s,k=map(str,input().split())
g=[]
a=s[int(k)-1]
#g.append(s[int(k)-1])
for i in range(0,len(s)):
	if s[i]==a:
		f=i
for i in range(f,len(s),int(k)):
	g.append(s[i])
print(*g)
