#G
s=input()
r=s[::-1]
for i in range(len(s)):
	if i!=len(s)-1:
		print(r[i],end="-")
	else:
		print(r[i])
