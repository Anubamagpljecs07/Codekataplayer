n=input()
s=list(n)
t=[]
for i in range(0,len(s)):
    if s[i].isupper():
        t.append(s[i].lower())
    elif s[i].islower():
        t.append(s[i].upper())
for j in t:
    print(j,end="")
