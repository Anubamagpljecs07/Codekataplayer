n,k=map(int,input().split())
l=list(map(int,input().split()))
g=[]
if k in l:
    print(k)
else:
    for i in l:
        if i<k:
            g.append(i)
    print(max(g))
    
