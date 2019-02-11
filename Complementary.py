l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s=input()
r=input()
g=[]
c=0
for i in s:
    g.append(i)
for i in r:
    g.append(i)
for i in g:
    if g.count(i)==1:
        c+=1
if c==26:
    print("complementary")
else:
    print("non-complementary")
