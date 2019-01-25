def issq(x):
    for j in range(0,1000):
        if pow(j,2)==x:
            a=0
            break
        else:
            a=1
    return a
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    if issq(i)==0:
        c+=1
print(c)
