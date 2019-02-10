s=input()
l=['1','2','3','4','5','6','7','8','9','A','E','I','O','U']
c=0
for i in s:
    if i in l:
        c+=1
if c==len(s):
    print("yes")
else:
    print("no")
