n,k=map(int,input().split())
l=list(map(int,input().split()))
if k in l:
    c=l.count(k)
    print("yes",c)
else:
    print("no")
