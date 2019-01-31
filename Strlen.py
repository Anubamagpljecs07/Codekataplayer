s=input()
l=list(s.split())
c=0
for i in l:
	for j in i:
		if j!="":
			c+=1
print(c)
