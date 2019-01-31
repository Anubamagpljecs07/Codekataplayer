m,n=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    for j in range(len(l)):
        if i!=j:
            if l[i]+l[j]==n:
                c+=1
                if c==1:
                    print("yes")
                    break
            if c==1:
                break
if c==0:
    print("no")
