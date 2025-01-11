a,b=map(int,input().split())
ba=[]
for k in range(1,a+1):
    ba.append(k)
for l in range(b):
    i,j=map(int,input().split())
    temp=ba[i-1:j]
    temp.reverse()
    ba[i-1:j]=temp
for p in range(a):
    print(ba[p], end=" ")