n=input()
c=0
for i in n:
    if i.isdigit():
        c+=1
    else:
        print("no")
        break
if c==len(n):
    print("yes")
