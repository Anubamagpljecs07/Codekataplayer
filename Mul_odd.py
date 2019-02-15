n=int(input())
l=list(map(int,input().split()))
g=1
for i in l:
    g=g*i
if g%2==1:
    print("odd")
else:
    print("even")
