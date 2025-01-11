a=[]
c=[]

for i in range(1,29):
    b=int(input())
    a.append(b)

for j in range(1,31):
    if j not in a:
        c.append(j)
    
print(min(c))
print(max(c))