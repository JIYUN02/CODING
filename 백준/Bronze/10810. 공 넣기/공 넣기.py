a,b=map(int,input().split())
c=[0]*a
for i in range(b):
    i,j,k=map(int,input().split())
    for p in range(i-1,j):
        c[p]=k
print(" ".join(map(str,c)))
    
    
    