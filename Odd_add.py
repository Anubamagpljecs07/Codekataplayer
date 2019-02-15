s=input()
g=[]
for i in s:
    if int(i)%2==1:
        g.append(int(i))
s=sum(g)
if s%2==0:
    print("E")
else:
    print("O")
