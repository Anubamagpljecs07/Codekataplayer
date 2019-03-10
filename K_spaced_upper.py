s,k=map(str,input().split())
s=list(s)
a=s[int(k)-1]
for i in range(0,len(s)):
	if s[i]==a:
		f=i
for i in range(f,len(s),int(k)):
	s[i]=s[i].upper()
g=""
for i in s:
	g=g+i
print(g)
