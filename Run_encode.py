s=input()
c=1
g=""
for i in range(0,len(s)):
    if i<len(s)-1:
        if s[i]==s[i+1]:
            c+=1
        elif s[i]!=s[i+1]:
            g=g+s[i]+str(c)
            c=1
    else:
        if s[i]==s[i-1]:
            g=g+s[i]+str(c)
        else:
            g=g+s[i]+str(1)
print(g)
