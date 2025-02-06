a,b=map(int,input().split())

map1=[]
for i in range(a):
    map1.append(list(map(int,input().split())))

map2=[]
for j in range(a):
    map2.append(list(map(int,input().split())))

for q in range(a):
    for w in range(b):
        result=map1[q][w]+map2[q][w]
        print(result,end=' ')
    print()