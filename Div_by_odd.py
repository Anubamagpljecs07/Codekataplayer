n=int(input())
c=0
if n%2==1:
    print(1)
else:
    for i in range(1,n+1):
        if n%i==0 and (n//i)%2==1:
            c+=1
            if c==1:
                print(i)
            
            
            
