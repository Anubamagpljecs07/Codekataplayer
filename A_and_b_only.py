s=input()
g=[]
for i in s:
	if i not in g:
		g.append(i)
l=['a','b']
if g==l:
	print("yes")
elif len(g)==1:
	if g[0]=="a" or g[0]=="b":
		print("yes")
elif len(g)==3:
	print("yes")
else:
	print("no")
