n,k=map(int,input().split())
l=list(map(int,input().split()))
if k in l:
    print(k)
else:
    for i in l:
        if i<k:
            print(i)
