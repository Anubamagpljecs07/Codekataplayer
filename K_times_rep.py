n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if l.count(i)==k:
        c+=1
        if c==1:
            print(i)
