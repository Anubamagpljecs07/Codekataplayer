n,k=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
for i in range(0,len(k)):
    l.append(k[i])
    m=max(l)
    c+=1
    if c==1:
        print(m,end="")
    else:
        print("",m,end="")
        
    
