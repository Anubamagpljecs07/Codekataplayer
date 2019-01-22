n,k=map(int,input().split())
p=n*k
c=0
for i in range(p,0,-1):
    if n%i==0 and k%i==0:
        c+=1
        if c==1:
            print(i)
