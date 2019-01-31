n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
g=[]
for i in l:
    for j in k:
        if i==j:
            g.append(i)
print(*g)
