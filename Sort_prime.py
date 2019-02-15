def isprime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        a=1
    else:
        a=0
    return a
n=int(input())
g=[]
for i in range(2,n+1):
    if n%i==0 and isprime(i)==1:
        g.append(i)
a=sorted(g)
print(*g)
