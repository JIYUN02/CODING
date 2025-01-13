a="abcdefghijklmnopqrstuvwxyz"
b=input()
c=[]

for i in a:
    if i in b:
        c.append(b.index(i))
    else:
        c.append(-1)
print(" ".join(map(str,c)))