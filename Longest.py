#G
s=input()
s=list(s.split())
l=[]
for i in s:
	l.append(len(i))
m=max(l)
for i in s:
	if len(i)==m:
		print(i)
		break
