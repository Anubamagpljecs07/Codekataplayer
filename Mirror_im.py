n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=[]
for i in range(len(l)-1,-1,-1):
    k.append(l[i])
if m==k:
    print("yes")
else:
    print("no")
