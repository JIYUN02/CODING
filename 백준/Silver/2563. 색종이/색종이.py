a=int(input())
array=[[0]*100 for _ in range(100)]

for i in range(a):
    n,m=map(int,input().split())
    
    for j in range(m,m+10):
        for k in range(n,n+10):
            array[j][k]=1
            
result=0
for nn in range(100):
    result+=array[nn].count(1)
    
print(result)
            