s="VishalSundar"
n=input()
g=[]
for i in n:
    if g.count(i)<s.count(i):
        g.append(i)
if len(g)==len(s):
    print("yes")
else:
    print("no")
