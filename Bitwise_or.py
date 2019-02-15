a,b=map(int,input().split())
p=a|b
d=bin(p)
c=d.count("1")
print(c)
