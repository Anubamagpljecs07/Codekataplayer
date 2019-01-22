n,k=map(int,input().split())
p=n*k
c=0
for i in range(1,p+1):
    if i%n==0 and i%k==0:
        c+=1
        if c==1:
            print(i)

        
