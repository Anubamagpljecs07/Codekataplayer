n=int(input())
l=list(map(int,input().split()))
g=sorted(l)
f=g[-1]-g[0]
print(f)
