s=input()
s=list(s.split())
b=input()
for i in s:
    if i==b:
        s.remove(i)
print(*s)
