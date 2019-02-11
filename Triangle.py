l=list(map(int,input().split()))
l=sorted(l)
if l[0]+l[1]>l[2]:
    print("yes")
else:
    print("no")
