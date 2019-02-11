l=list(map(int,input().split()))
l=sorted(l)
a=l[0]*l[0]
b=l[1]*l[1]
c=l[2]*l[2]
if a+b==c:
    print("yes")
else:
    print("no")
