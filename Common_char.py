r,s=map(str,input().split())
c=0
for i in range(0,len(r)):
    for j in range(0,len(s)):
        if r[i]==s[j]:
            c+=1
            if c==1:
                print("yes")
                break
        if c==1:
            break
if c==0:
    print("no")
